import func_arb
import json

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

    # Print out the amout of all tradingpairs and the amount after checking if they are tradable
    print("All the pairs that can be traded - ", "Full list: ",
          len(coin_json), " Cleaned up list: ", len(coin_list))

    # Return list of tradeable coins
    return coin_list


"""
    Step 1: Structuring Triangluar Pairs
    Calculation only
"""


def step_1(coin_list):

    # Structure the list of tradeable triangular arbitrage pairs
    structured_list = func_arb.structure_triangular_pairs(coin_list)

    # Save structured list
    with open("Udemy/data/structured_triangular_pairs.json", "w") as fp:
        json.dump(structured_list, fp)


""" Main """
if __name__ == "__main__":
    coin_list = step_0()
    structured_pairs = step_1(coin_list)
    # step_1()
    # step_2()
    # step_3()
    # step_4()
