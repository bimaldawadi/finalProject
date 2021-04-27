 LibraryManagementSystem
This Application is developed on BootStrap, Python- Flask with MySQL. This is a web-based application which regulates each and every function of Library. So this can be used in any library.

Query that will be used:

CREATE DATABASE library;

USE library;

CREATE TABLE employee(employee_id INT AUTO_INCREMENT PRIMARY KEY, employeeName VARCHAR(100), employeeUsername VARCHAR(100), password VARCHAR(150) );

select * from employee;

CREATE TABLE customer(customer_id INT PRIMARY KEY AUTO_INCREMENT, customerName VARCHAR(100), email VARCHAR(100),  mobile VARCHAR(12), customerUsername VARCHAR(100), password VARCHAR(50));

select * from customer;

CREATE TABLE books(book_id INT PRIMARY KEY AUTO_INCREMENT, bookName VARCHAR(100), author VARCHAR(100), addedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, available BOOL DEFAULT 1);

select * from books;

CREATE TABLE transactions(transaction_id INT AUTO_INCREMENT PRIMARY KEY, customerUsername VARCHAR(100), employeeUsername VARCHAR(100), book_id INT(11), bookName VARCHAR(100), issueDate DATETIME, returnDate DATETIME, fine INT DEFAULT 0, Done INT);

select * from transactions;


INSERT INTO books VALUES(bookName)(("Python flask")("Softwre Engineering"));
