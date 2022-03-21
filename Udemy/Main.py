import func_arb

"""
    Step 0: Finding coins which can be traded
    Exchange: Poloniex
    https://docs.poloniex.com/#introduction 
"""


def step_0():

    # Extract list of coins and prices from Exchange
    url = "https://poloniex.com/public?command=returnTicker"
    coin_json = func_arb.get_coin_tickers(url)

    # Loop trough each objects and find the tradable pairs
    coin_list = func_arb.collect_tradeables(coin_json)

    print(coin_list)
    print(len(coin_json), len(coin_list))

    return coin_list


""" Main """
if __name__ == "__main__":
    coin_list = step_0()

    # step_1()
    # step_2()
    # step_3()
    # step_4()
