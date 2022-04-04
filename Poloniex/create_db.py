import sqlite3

# Documentation can be found here: https://docs.python.org/3/library/sqlite3.html
# Connect to database 'database.db' or create one if it doesn't exist.
conn = sqlite3.connect('Udemy/data/database.db')

# Create a cursor for db
cursor = conn.cursor()

# Create a table
cursor.execute("""CREATE TABLE trades (
    timestamp,
    surface_rate_profit_loss_perc,
    real_rate_profit_loss_perc,
    contract_1,
    contract_2,
    contract_3
    )""")

# DATATYPE for sqlite = NULL, INTEGER, REAL, TEXT, BLOB

# Commit our command
conn.commit()

# Close our connection
conn.close()
