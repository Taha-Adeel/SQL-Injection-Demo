# SQL-Injection-Demo

## Description

This project was done for Kludge, the Information Security and Networking Club of IIT Hyderabad.
<br /><br /> 
SQL is a language employed in websites to interact with databases. It allows the website to create, retrieve, update and delete database records.
<br /> 
An SQL injection is a security vulnerability that allows an attacker to inject malicious SQL statements into a web application's input fields and gain unauthorized access to sensitive data such as usernames, passwords and credit card credentials.
<br/><br/>
In this project, we demonstrate how SQL injection attacks work and the measures taken to mitigate them.

## Installation and setup

* First install flask and mySQL: </br> 
`pip3 install flask` </br>
`pip3 install mysql-connector-python`

* You also need to ensure your system has mySQL. Install it with the command `sudo apt-get install mysql-server` if mysql is not present. You will also need to configure the root password for mySQL (google). Then in app.py, change the values of username and password to your mySQL root username and password.

* Then run the following commands to create the database and table:</br>
`mysql -u root -p`   # enter your password when prompted (configured above) </br>
`CREATE DATABASE users_db;` </br>
`USE users_db;` </br>
`CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255));` </br>
`INSERT INTO users (username, password) VALUES ('admin', 'password');` </br>
`INSERT INTO users (username, password) VALUES ('user', 'password');` </br>
`INSERT INTO users (username, password) VALUES ('test', 'password');` 


* Then run the following command to start the server: </br>
`python3 app.py`
