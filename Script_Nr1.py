import os
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

candles1min = client.get_historical_klines(
    "BTCUSDT", Client.KLINE_INTERVAL_1MINUTE, "1 minute ago UTC")


# candles1min_pd = pd.DataFrame(columns=['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time',
#                                        'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'])

candles1min_pd = pd.DataFrame({'Open time': candles1min[0][0], 'Open': candles1min[0][1], 'High': candles1min[0][2],
                               'Low': candles1min[0][3], 'Close': candles1min[0][4], 'Volume': candles1min[0][5],
                               'Close time': candles1min[0][6], 'Quote asset volume': candles1min[0][7],
                               'Number of trades': candles1min[0][8], 'Taker buy base asset volume': candles1min[0][9],
                               'Taker buy quote asset volume': candles1min[0][10], 'Ignore': candles1min[0][11]}, index=[0])


print(candles1min_pd)

# # Get 24h candle
# candles = client.get_ticker(symbol='BTCUSDT')
# candles_pd = pd.DataFrame.from_dict(candles, orient='index')
# print(candles_pd)
