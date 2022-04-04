import sqlite3


def write_trade_in_db(timestamp, surface_rate_profit_loss_perc, real_rate_profit_loss_perc, contract_1, contract_2, contract_3):

    # Connect to database 'database.db'
    conn = sqlite3.connect('Poloniex/data/database.db')

    # Create a cursor for db
    cursor = conn.cursor()

    # write a table to store in the database
    trades = [(timestamp, surface_rate_profit_loss_perc,
               real_rate_profit_loss_perc, contract_1, contract_2, contract_3)]

    cursor.executemany(
        "INSERT INTO trades VALUES (?,?,?,?,?,?)", trades)

    # Commit our command
    conn.commit()

    # Close our connection
    conn.close()
