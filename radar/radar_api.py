import json
import pprint as pp

import requests

from radar_book import RadarBook
from src.exceptions import ExchangeException
from src.constants import tokens

MARKETS_ENDPOINT = 'https://api.radarrelay.com/v2/markets'
ORDERBOOK_ENDPOINT = 'https://api.radarrelay.com/v2/markets/{marketID}/book'
TOKENS_ENDPOINT = 'https://api.radarrelay.com/v2/tokens'


def get_markets():
    me = MARKETS_ENDPOINT
    payload = {'perPage': 100, 'page': 1}  # Max 100 markets per page
    r = requests.get(me, params=payload)

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
        raise ExchangeException(message="Invalid request status code {}".format(r.status_code),
                                status_code=r.status_code)


def get_token_list():
    tle = TOKENS_ENDPOINT
    r = requests.get(tle)

    if r.status_code == 200:
        r_json = json.loads(r.text)
        return [str(t['symbol']) for t in r_json]

    else:
        raise ExchangeException(message="Invalid request status code {}".format(r.status_code),
                                status_code=r.status_code)


def main():
    # toks = tokens.values()
    # vals = []
    # for tok in toks:
    #     if tok not in ['WETH', 'DAI']:
    #         print tok
    #         book = load_book_for_market('{}-WETH'.format(tok))
    #         vals.append((tok, book.asks, book.bids))
    # pp.pprint(vals)
    a = load_book_for_market('VEE-WETH')
    pp.pprint([a.asks, a.bids])


if __name__ == '__main__':
    main()
0.000041810157640108