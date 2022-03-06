import sqlite3

# Connect to database 'database.db'
conn = sqlite3.connect('database.db')

# Create a cursor for db
cursor = conn.cursor()

# rowid is a Primary Key which all rows have. We can see it if we select 'rowid'
cursor.execute("SELECT rowid, * FROM orders")

# fetch it from the db and print it to the console
orders = cursor.fetchall()

# makes the output more readable in the console...
for order in orders:
    print(order)

# Commit our command
conn.commit()

# Close our connection
conn.close()
