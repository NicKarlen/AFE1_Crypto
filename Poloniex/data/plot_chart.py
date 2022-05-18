import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from datetime import date

# Create a connection to the database
con = sqlite3.connect('Poloniex/data/database.db')
# query the db and return a dataframe
df = pd.read_sql_query(f"SELECT * FROM trades", con)
# close the connection to the database
con.close()

df = df.head(964)
# Output the plots
df.plot(kind='line', x="timestamp", y=["surface_rate_profit_loss_perc", "real_rate_profit_loss_perc"], xlabel='Timestamp', ylabel="Profit in %", legend=True)
# Adjust the spacing at the bottom of the window
plt.subplots_adjust(bottom=0.3)
# Set main titel above all subplots
plt.title("Mögliche Trianguläre Arbitrage Trades über 24h auf Poloniex")
# Show the plot
plt.show()    