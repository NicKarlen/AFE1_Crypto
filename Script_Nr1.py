from binance import Client
import pandas as pd

# function to get the api_keys from the locally safed file


def getApiAccessKey(filename):
    with open('API_Keys/'+filename) as f:
        api_key, api_secret = next(f), next(f)

    return {
        "api_key": api_key[:-1],
        "api_secret": api_secret
    }


BinanceApiKeys = getApiAccessKey('Binance_key.txt')

client = Client(BinanceApiKeys['api_key'], BinanceApiKeys['api_secret'])

# print(BinanceApiKeys['api_key'])
# print(BinanceApiKeys['api_secret'])

# continue
# https://youtu.be/_IV1qfSPPwI?t=318


candles = client.get_ticker(symbol='BTCUSDT')

candlespd = pd.DataFrame.from_dict(candles, orient='index')

print(candlespd)
