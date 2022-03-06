from sre_compile import isstring
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


print(getApiAccessKey('Binance_key.txt')['api_key'])
print(getApiAccessKey('Binance_key.txt')['secret_key'])
