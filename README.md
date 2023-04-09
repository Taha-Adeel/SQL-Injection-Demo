# SQL-Injection-Demo

First install flask and mySQL: \
`pip3 install flask` \
`pip3 install mysql-connector-python`

Then run the following commands to create the database and table:\
`mysql -u root -p` \
`CREATE DATABASE demo;` \
`USE demo;` \
`CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255));` \
`INSERT INTO users (username, password) VALUES ('admin', 'password');` \
`INSERT INTO users (username, password) VALUES ('user', 'password');` \
`INSERT INTO users (username, password) VALUES ('test', 'password');` 


Then run the following command to start the server: \
`python3 app.py`
