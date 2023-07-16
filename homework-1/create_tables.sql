-- SQL-команды для создания таблиц
CREATE TABLE customers
(
customer_id char(5) PRIMARY KEY NOT NULL,
company_name varchar(100),
contact_name varchar(100)
);

CREATE TABLE employees
(
employee_id int PRIMARY KEY NOT NULL,
first_name varchar(100),
last_name varchar(100),
title varchar(100),
birth_date date,
notes text
);

CREATE TABLE orders
(
order_id int PRIMARY KEY NOT NULL,
customer_id char(5) REFERENCES customers(customer_id) NOT NULL,
employee_id int REFERENCES employees(employee_id) NOT NULL,
order_date date,
ship_city varchar(100)
);