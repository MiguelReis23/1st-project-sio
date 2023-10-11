import sqlite3

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('online_shop.db')

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
c.execute('''CREATE TABLE IF NOT EXISTS customers
             (id INTEGER PRIMARY KEY,
              name TEXT NOT NULL,
              email TEXT)''')

# Create a table for user login information
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY,
              username TEXT,
              password TEXT,
              permission TEXT,
              FOREIGN KEY (username) REFERENCES customers(name))''')

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


# Save changes and close the connection
conn.commit()
conn.close()

