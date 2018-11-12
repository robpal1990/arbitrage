import pprint as pp

from bancor.bancor_api import get_token_price as bancor_price
from radar.radar_api import load_book_for_market as radar_price

def check_if_triangluar_arbitrage(curr_a, curr_b, curr_c):
    pass


def get_many_prices(ticker):
    pp.pprint('BANCOR PRICE: {} WETH'.format(bancor_price(ticker)))
    pp.pprint(radar_price('{}-WETH'.format(ticker)).bids[0])
    pp.pprint(radar_price('{}-WETH'.format(ticker)).asks[0])

def main():
    get_many_prices('DRT')



if __name__ == "__main__":
    main()