# SQL-Injection-Demo

## Description

This project was done for Kludge, the Information Security and Networking Club of IIT Hyderabad.
<br /><br /> 
SQL is a language employed in websites to interact with databases. It allows the website to create, retrieve, update and delete database records.
<br /> 
An SQL injection is a security vulnerability that allows an attacker to inject malicious SQL statements into a web application's input fields and gain unauthorized access to sensitive data such as usernames, passwords and credit card credentials.
<br/><br/>
In this project, we demonstrate how SQL injection attacks work and the simple measures to mitigate them.

## Demo
Below is a simple example of running an SQL injection attack on the login page, with and without mitigation. <br>

1. Without mitigation: </br>
	&nbsp; <img src="./static/vulnerable.png" width="600"> <br>
	&nbsp; As we can see, we are able to login without knowing the password.

2. With mitigation: </br>
	&nbsp; <img src="./static/secure.png" width="600"> <br>
	&nbsp; The attack is blocked as we sanitize the input before executing the SQL query. 

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
`INSERT INTO users (username, password) VALUES ('admin', 'password1');` </br>
`INSERT INTO users (username, password) VALUES ('user', 'password2');` </br>
`INSERT INTO users (username, password) VALUES ('test', 'password3');`  </br>
`INSERT INTO users (username, password) VALUES ('kludge', 'p@ssw0rd');`


* Then run the following command to start the server: </br>
`python3 app.py`
