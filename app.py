from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists in the database
        mycursor = mydb.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        values = (username, password)
        mycursor.execute(query, values)
        user = mycursor.fetchone()

        if user:
            # If the username and password match, log the user in
            session['user_id'] = user[0]
            return redirect(url_for('index'))
        else:
            # If the username and password don't match, show an error message
            error = 'Invalid username or password. Please try again.'
            return render_template('login.html', error=error)

    else:
        # If the request method is GET, show the login page
        return render_template('login.html')

# Route for index page
@app.route('/')
def index():
    # Check if the user is logged in
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']

    # Retrieve the user's data from the database
    mycursor = mydb.cursor()
    query = "SELECT * FROM users WHERE id = %s"
    values = (user_id,)
    mycursor.execute(query, values)
    user = mycursor.fetchone()

    # Render the index page with the user's data
    return render_template('index.html', user=user)

# Route for logout
@app.route('/logout')
def logout():
    # Clear the session variable and redirect to the login page
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
