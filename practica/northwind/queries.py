query_create_table_users = """
CREATE TABLE users (
    customer_id NVARCHAR(10) PRIMARY KEY, 
    company_name NVARCHAR(100) NOT NULL, 
    contact_name NVARCHAR(50) NOT NULL
);
"""

query_create_table_employees_data = """
CREATE TABLE employees_data (
    employee_id INT IDENTITY(1, 1) PRIMARY KEY, 
    first_name NVARCHAR(100) NOT NULL, 
    last_name NVARCHAR(100) NOT NULL, 
    title NVARCHAR(100) NOT NULL, 
    birth_data DATE NOT NULL, 
    notes NVARCHAR(1000) NOT NULL
);
"""

query_create_table_orders_data = """
CREATE TABLE orders_data (
    order_id INT PRIMARY KEY, 
    customer_id NVARCHAR(10) NOT NULL, 
    employee_id INT NOT NULL, 
    order_date DATE NOT NULL, 
    ship_city NVARCHAR(100) NOT NULL, 
    FOREIGN KEY (customer_id) REFERENCES users(customer_id), 
    FOREIGN KEY (employee_id) REFERENCES employees_data(employee_id)
);
"""


insert_query_customers_table = """
INSERT INTO users (
    customer_id, 
    company_name, 
    contact_name
) VALUES (?, ?, ?);
"""

insert_query_employees_table = """
INSERT INTO employees_data (
    first_name, 
    last_name, 
    title, 
    birth_data, 
    notes
) VALUES (?, ?, ?, ?, ?);
"""

insert_query_orders_table= """
INSERT INTO orders_data (
    order_id,
    customer_id, 
    employee_id, 
    order_date, 
    ship_city
) VALUES (?, ?, ?, ?, ?);
"""
