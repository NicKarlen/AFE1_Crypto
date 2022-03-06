import sqlite3

# Connect to database 'database.db'
conn = sqlite3.connect('database.db')

# Create a cursor for db
cursor = conn.cursor()

# Where clause
cursor.execute("SELECT * FROM orders WHERE tradingpair LIKE '%USD'")

# cursor.execute("SELECT * FROM orders WHERE tradingpair LIKE 'ETH%'")
#cursor.execute("SELECT * FROM orders WHERE price > 38500")

# fetch it from the db and print it to the console
orders = cursor.fetchall()

# makes the output more readable in the console...
for order in orders:
    print(order)

# Close our connection
conn.close()
