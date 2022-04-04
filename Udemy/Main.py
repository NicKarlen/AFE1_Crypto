import func_arb
import json
import time
from datetime import datetime
import write_db

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
        if len(surface_arb) > 0:
            real_rate_arb = func_arb.get_depth_from_orderbook(surface_arb)
            if len(real_rate_arb) > 0:
                if real_rate_arb["real_rate_perc"] > 0.05:

                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    write_db.write_trade_in_db(current_time, surface_arb["profit_loss_perc"], real_rate_arb["real_rate_perc"],
                                               real_rate_arb["contract_1"], real_rate_arb["contract_2"], real_rate_arb["contract_3"])

                    print("NEW TRADE:", surface_arb["direction"], " Surface profit percent= ",
                          surface_arb["profit_loss_perc"], "  Timestamp: ", current_time)
                    print(real_rate_arb)


""" Main """
if __name__ == "__main__":
    # coin_list = step_0()
    # step_1(coin_list)
    while True:
        step_2()

    print("code done -----------!!!!!!!!!!!!!!!!!")
