import sqlite3

# Connect to database 'database.db'
conn = sqlite3.connect('database.db')

# Create a cursor for db
cursor = conn.cursor()

# Read something in the database
cursor.execute("SELECT * FROM orders")

# fetch it from the db and print it to the console
orders = cursor.fetchall()

# makes the output more readable in the console...
for order in orders:
    print(order)

# Commit our command
conn.commit()

# Close our connection
conn.close()
