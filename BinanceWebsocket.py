import json
import os
import websockets
import asyncio
from datetime import datetime

# function to get the api_keys from the locally safed file


def getApiAccessKey(filename):
    with open('API_Keys/'+filename) as f:
        api_key, api_secret = next(f), next(f)

    return {
        "api_key": api_key[:-1],
        "api_secret": api_secret
    }


BinanceApiKeys = getApiAccessKey('Binance_key.txt')


# Documentation for websockets and the url's where found here: https://binance-docs.github.io/apidocs/futures/en/#websocket-market-streams

async def listen():
    url = "wss://fstream.binance.com/stream?streams=btcusdt@aggTrade/btcusdt@markPrice"

    async with websockets.connect(url) as ws:
        while True:
            msg = await ws.recv()
            d = json.loads(msg)
            print(d['data']['p'])
            print('Timestamp API call:  ' + str(datetime.now()))

asyncio.get_event_loop().run_until_complete(listen())
