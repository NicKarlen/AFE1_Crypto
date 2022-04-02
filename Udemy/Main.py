import func_arb
import json
import time

# Set Variables

coin_price_url = "https://poloniex.com/public?command=returnTicker"

"""
    Step 0: Finding coins which can be traded
    Exchange: Poloniex
    https://docs.poloniex.com/#introduction
"""


def step_0():

    # Extract list of coins and prices from Exchange
    coin_json = func_arb.get_coin_tickers(coin_price_url)

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


"""
    Step 2: Calculate surface-rate Arbitrage Opportunities
"""


def step_2():

    # Get Structured Pairs
    with open("Udemy/data/structured_triangular_pairs.json") as json_file:
        structured_pairs = json.load(json_file)

    # Get latest surface prices
    prices_json = func_arb.get_coin_tickers(coin_price_url)

    # Loop through and get structured price information
    for t_pair in structured_pairs:
        prices_dict = func_arb.get_price_for_t_pair(t_pair, prices_json)
        surface_arb = func_arb.calc_triangular_arb_surface_rate(
            t_pair, prices_dict)
        if len(surface_arb) and surface_arb["profit_loss_perc"] > 0.3:
            print("NEW TRADE:")
            print(surface_arb["trade_description_1"])
            print(surface_arb["trade_description_2"])
            print(surface_arb["trade_description_3"])
            print(surface_arb["profit_loss_perc"])


""" Main """
if __name__ == "__main__":
    # coin_list = step_0()
    # step_1(coin_list)
    # step_2()
    real_rate_arb = func_arb.get_depth_from_orderbook()
    # step_4()
    print(real_rate_arb)
    print("code done -----------!!!!!!!!!!!!!!!!!")
