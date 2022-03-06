from binance import Client
import pandas as pd

# function to get the api_keys from the locally safed file


def getApiAccessKey(filename):
    with open('API_Keys/'+filename) as f:
        api_key, secret_key = next(f), next(f)

    return {
        "api_key": api_key[:-1],
        "secret_key": secret_key
    }


BinanceApiKeys = getApiAccessKey('Binance_key.txt')

print(BinanceApiKeys['api_key'])
print(BinanceApiKeys['secret_key'])

# continue
# https://youtu.be/_IV1qfSPPwI?t=318
