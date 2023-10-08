import sqlite3

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('online_shop.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Create a table for products
c.execute('''CREATE TABLE products
             (id INTEGER PRIMARY KEY,
              name TEXT,
              description TEXT,
              price REAL,
              stock INTEGER)''')

# Create a table for customers
c.execute('''CREATE TABLE customers
             (id INTEGER PRIMARY KEY,
              name TEXT,
              email TEXT)''')

# Create a table for orders
c.execute('''CREATE TABLE orders
             (id INTEGER PRIMARY KEY,
              customer_id INTEGER,
              product_id INTEGER,
              quantity INTEGER,
              FOREIGN KEY (customer_id) REFERENCES customers(id),
              FOREIGN KEY (product_id) REFERENCES products(id))''')

# Create a table for user login information
c.execute('''CREATE TABLE users
             (id INTEGER PRIMARY KEY,
              username TEXT,
              password TEXT,
              FOREIGN KEY (username) REFERENCES customers(name))''')

# Save changes and close the connection
conn.commit()
conn.close()

