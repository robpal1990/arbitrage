import json
import pprint as pp

import requests

from radar_book import RadarBook
from src.exceptions import ExchangeException

MARKETS_ENDPOINT = 'https://api.radarrelay.com/v2/markets'
ORDERBOOK_ENDPOINT = 'https://api.radarrelay.com/v2/markets/{marketID}/book'


def get_markets():
    me = MARKETS_ENDPOINT
    r = requests.get(me)

    if r.status_code == 200:
        r_json = json.loads(r.text)
        markets = [market['id'] for market in r_json]

        return markets

    else:
        raise ExchangeException("Invalid request status code {}".format(r.status_code),
                                status_code=r.status_code)


def load_book_for_market(marketID):
    oe = ORDERBOOK_ENDPOINT.format(marketID=marketID)
    r = requests.get(oe)

    if r.status_code == 200:
        r_json = json.loads(r.text)
        book = RadarBook.load_from_market_pair(marketID, **r_json)
        return book

    else:
        raise ExchangeException("Invalid request status code {}".format(r.status_code),
                                status_code=r.status_code)

#
# def main():
#     markets = get_markets()
#     # print markets
#     # full_book = map(load_book_for_market, markets)
#     full_book = load_book_for_market('BAT-WETH')
#     pp.pprint(full_book.asks)
#     pp.pprint(full_book.bids)
#
#
# if __name__ == '__main__':
#     main()