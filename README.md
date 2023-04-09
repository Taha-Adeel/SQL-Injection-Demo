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

* First install flask and mySQL: \
`pip3 install flask` \
`pip3 install mysql-connector-python`

* Then run the following commands to create the database and table:\
`mysql -u root -p` \
`CREATE DATABASE demo;` \
`USE demo;` \
`CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255));` \
`INSERT INTO users (username, password) VALUES ('admin', 'password');` \
`INSERT INTO users (username, password) VALUES ('user', 'password');` \
`INSERT INTO users (username, password) VALUES ('test', 'password');` 


* Then run the following command to start the server: \
`python3 app.py`
