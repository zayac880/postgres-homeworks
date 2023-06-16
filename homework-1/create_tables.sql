-- SQL-команды для создания таблиц
-- Создание таблицы "employees"
CREATE TABLE employees (
  employee_id INT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  title TEXT,
  birth_date DATE,
  notes TEXT
);

-- Создание таблицы "customers"
CREATE TABLE customers (
  customer_id VARCHAR(100) PRIMARY KEY,
  company_name VARCHAR(100),
  contact_name VARCHAR(100)
);

-- Создание таблицы "orders"
CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id VARCHAR(100),
  employee_id INT,
  order_date DATE,
  ship_city VARCHAR(100),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
  FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
);
