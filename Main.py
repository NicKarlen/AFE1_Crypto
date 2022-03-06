import sqlite3

# sqlite is a fast light weight sql database, which comes with python. It doesn't need any extra service.
# Connect to database 'database.db' or create one if it doesn't exist.
conn = sqlite3.connect('database.db')

# Create a cursor for db
cursor = conn.cursor()

# Create a table
cursor.execute("""CREATE TABLE customers (
    order_ID DATATYPE,
    order_type DATATYPE,
    tradingpair DATATYPE,
    amount DATATYPE,
    price DATATYPE,
    time DATATYPE,
    )""")
