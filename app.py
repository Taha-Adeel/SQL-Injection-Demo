from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key' # Value used to encrypt the session cookies. You can change this value to anything you want.

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root", # Change this to your MySQL username
  password="password", # Change this to your MySQL password
  database="users_db"
)

# Run the sql query to find the user with the given username and password without sanitizing the input
def find_user_unsafe(username: str, password: str):
    mycursor = mydb.cursor()
    query = 'SELECT * FROM users WHERE username ="' + username + '" AND password ="' + password + '"'
    mycursor.execute(query)
    user = mycursor.fetchall()
    return user, query

# Run the sql query to find the user with the given username and password by using parameterized queries, hence ensuring the input is sanitized
def find_user_safe(username: str, password: str):
    mycursor = mydb.cursor()
    query = 'SELECT * FROM users WHERE username = %s AND password = %s'
    values = (username, password)
    mycursor.execute(query, values)
    query_str = mycursor.statement
    user = mycursor.fetchall()
    return user, query_str

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        protection_choice = request.form['protection_choice']

        if protection_choice == 'safe':
            user, query = find_user_safe(username, password)
        else:
            user, query = find_user_unsafe(username, password)

        if user:
            # If the user exists, store the user id in the session
            session['user_id'] = user[0][0]
            flash('Logged in successfully.')
        else:
            # If the user does not exist, show an error message
            flash('Incorrect username or password.')
            

        return render_template('login.html', user=user, query=query)

    else:
        # If the request method is GET, show the login page
        return render_template('login.html')

# Route for base page
@app.route('/')
def home():
    return redirect(url_for('login'))

# Route for logout
@app.route('/logout')
def logout():
    # Clear the session variable and redirect to the login page
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)