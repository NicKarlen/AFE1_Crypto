import requests
import json


# Make a get request
def get_coin_tickers(url):
    req = requests.get(url)
    json_response = json.loads(req.text)
    if req.status_code != 200:
        print("requst from get_coin_ticker was not sucsessful, Code: " + req.status_code)
    else:
        return json_response


def collect_tradeables(json_obj):
    coin_list = []
    for coin in json_obj:
        is_frozen = json_obj[coin]["isFrozen"]
        is_post_only = json_obj[coin]["postOnly"]
        if is_frozen == "0" and is_post_only == "0":
            coin_list.append(coin)
    return coin_list
