import sqlite3

# sqlite is a fast light weight sql database, which comes with python. It doesn't need any extra service.
# Documentation can be found here: https://docs.python.org/3/library/sqlite3.html
# Youtube tutorial I used is: https://www.youtube.com/watch?v=byHcYRpMgI4&t=884s
# Connect to database 'database.db' or create one if it doesn't exist.
conn = sqlite3.connect('database.db')

# Create a cursor for db
cursor = conn.cursor()

# Create a table
cursor.execute("""CREATE TABLE orders (
    order_ID integer,
    order_type text,
    tradingpair text,
    amount integer,
    price integer,
    time text
    )""")

# DATATYPE for sqlite = NULL, INTEGER, REAL, TEXT, BLOB

# Commit our command
conn.commit()

# Close our connection
conn.close()
