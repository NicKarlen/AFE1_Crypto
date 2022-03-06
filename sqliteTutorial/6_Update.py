import sqlite3

# Connect to database 'database.db'
conn = sqlite3.connect('database.db')

# Create a cursor for db
cursor = conn.cursor()

# Update records
cursor.execute("""UPDATE orders SET price = 60000
                WHERE rowid = 1
                """)

# Commit our command
conn.commit()

# Where clause
cursor.execute("SELECT * FROM orders")


# fetch it from the db and print it to the console
orders = cursor.fetchall()

# makes the output more readable in the console...
for order in orders:
    print(order)


# Close our connection
conn.close()
