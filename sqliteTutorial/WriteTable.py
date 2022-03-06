import sqlite3

# Connect to database 'database.db'
conn = sqlite3.connect('database.db')

# Create a cursor for db
cursor = conn.cursor()

# write into a table
cursor.execute(
    "INSERT INTO orders VALUES ('2','BUY','BTCUSD','100','38400','06.03.2022,15:08:58')")

# DATATYPE for sqlite = NULL, INTEGER, REAL, TEXT, BLOB

# Commit our command
conn.commit()

# Close our connection
conn.close()
