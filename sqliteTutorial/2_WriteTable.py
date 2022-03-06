import sqlite3

# Connect to database 'database.db'
conn = sqlite3.connect('database.db')

# Create a cursor for db
cursor = conn.cursor()

# write a table to store in the database
many_orders = [('3', 'BUY', 'BTCUSD', '100', '38400', '06.03.2022,15:09:58'),
               ('4', 'BUY', 'BTCUSD', '120', '38500', '06.03.2022,15:10:58'),
               ('5', 'SELL', 'BTCUSD', '150', '38700', '06.03.2022,15:11:58')]

# executemany will help to insert many rows all at ones
cursor.executemany(
    "INSERT INTO orders VALUES (?,?,?,?,?,?)", many_orders)

# write into a table when you only want to insert one row

# cursor.execute(
#    "INSERT INTO orders VALUES ('2','BUY','BTCUSD','100','38400','06.03.2022,15:08:58')")


# Commit our command
conn.commit()

# Close our connection
conn.close()
