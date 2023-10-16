import sqlite3
import os

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('online_shop.db')
DB_STRING = "app.db"

db_directory = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(db_directory, DB_STRING)

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Create a table for products
c.execute('''CREATE TABLE IF NOT EXISTS products
             (id INTEGER PRIMARY KEY,
              name TEXT,
              description TEXT,
              category TEXT,
              price REAL,
              stock INTEGER)''')

# Create a table for customers
c.execute('''CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(50) NOT NULL DEFAULT '',
            last_name VARCHAR(50) NOT NULL DEFAULT '', 
            phone_number CHAR(9) NOT NULL DEFAULT '',
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL)''')

# Create a table for orders
c.execute('''CREATE TABLE IF NOT EXISTS orders
             (id INTEGER PRIMARY KEY,
              customer_id INTEGER,
              product_id INTEGER,
              quantity INTEGER,
              FOREIGN KEY (customer_id) REFERENCES customers(id),
              FOREIGN KEY (product_id) REFERENCES products(id))''')

# Create a table for payments
c.execute('''CREATE TABLE IF NOT EXISTS payments
             (id INTEGER PRIMARY KEY,
              customer_id INTEGER,
              order_id INTEGER,
              amount REAL,
              FOREIGN KEY (customer_id) REFERENCES customers(id),
              FOREIGN KEY (order_id) REFERENCES orders(id))''')

# Create a table for reviews
c.execute('''CREATE TABLE IF NOT EXISTS reviews
             (id INTEGER PRIMARY KEY,
              product_id INTEGER,
              customer_id INTEGER,
              rating INTEGER,
              review TEXT,
              FOREIGN KEY (product_id) REFERENCES products(id),
              FOREIGN KEY (customer_id) REFERENCES customers(name))''')


def show_database():
    users_table = " SELECT * FROM users; "

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(users_table)
        for row in cursor.fetchall():
            print(row)

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        for row in cursor.fetchall():
            print(row)

def clean_database():
    users_table = " DROP TABLE IF EXISTS users;"

    with sqlite3.connect(db_path) as conn:
        conn.execute(users_table)

# Save changes and close the connection
conn.commit()
conn.close()

