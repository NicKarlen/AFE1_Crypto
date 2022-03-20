# Step 0: gather correct coins

"""
    Step 0: Finding coins which can be traded
    Exchange: Poloniex
    https://docs.poloniex.com/#introduction 
"""

import requests

url = "https://poloniex.com/public?command=returnTicker"

req = requests.get(url)
print(req)
