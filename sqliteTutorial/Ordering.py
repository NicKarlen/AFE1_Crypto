import sqlite3

# Connect to database 'database.db'
conn = sqlite3.connect('database.db')

# Create a cursor for db
cursor = conn.cursor()

# Query the database - order by
cursor.execute("SELECT rowid, * FROM orders ORDER BY price AND time")


# fetch it from the db and print it to the console
orders = cursor.fetchall()

# makes the output more readable in the console...
for order in orders:
    print(order)

# Close our connection
conn.close()
