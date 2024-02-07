-- use .read filename to run this file!

-- sqlite3 <databasename>.db to create a database

-- Drop tables
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS orders;

-- create some tables

-- CREATE TABLE IF NOT EXISTS <tablename>(
--     id INTEGER PRIMARY KEY,
--     <attribute1> TEXT,
--     <attribute2> INTEGER
-- );

-- CREATE TABLE IF NOT EXISTS <tablename2>(
--     id INTEGER PRIMARY KEY,
--     <attribute1> TEXT,
--     <attribute2> INTEGER,
--     <tablename_id> INTEGER,
--     FOREIGN KEY (tablename_id) REFERENCES tablename(id)
-- );

CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
);

CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantitiy INTEGER,
    total_price REAL,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- insert some values into the database
INSERT INTO customers (name, email) VALUES 
("John Doe", "john@gmail.com"), 
("Jane Smith", "smith@gmail.com"), 
("Mick Johnson", "michael@gmail.com");

INSERT INTO products (name, price) VALUES 
("Smart Watch", 500.00), 
("Wireless Headset", 79.80), 
("Camera", 350.99),
("TV", 299.99),
("Speaker", 149.99);

INSERT INTO orders (customer_id, product_id, quantitiy, total_price, order_date) VALUES 
(1, 1, 1, 299.99, "2024-02-05"),
(2, 2, 2, 199.99, "2024-02-06"),
(3, 3, 1, 129.99, "2024-02-07");

