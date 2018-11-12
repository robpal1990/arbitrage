import requests
import json
import pprint as pp

from src.constants import tokens
from src.exceptions import ExchangeException

TOKENS_ENDPOINT = 'https://api.bancor.network/0.1/currencies/convertiblePairs'
PRICE_ENDPOINT = 'https://api.bancor.network/0.1/currencies/{quoteToken}/ticker?fromCurrencyCode=ETH&displayCurrencyCode=ETH'

def get_token_list():
    tle = TOKENS_ENDPOINT
    r = requests.get(tle)

    if r.status_code == 200:
        r_json = json.loads(r.text)
        tokens = r_json['data'].keys()
        return sorted([str(tok) for tok in tokens if str(tok)[-3:] != 'BNT'] + ['BNT'])

    else:
        raise ExchangeException(message="Invalid request status code {}".format(r.status_code),
                                status_code=r.status_code)


def get_token_price(ticker):
    pe = PRICE_ENDPOINT.format(quoteToken=ticker)
    r = requests.get(pe)

    if r.status_code == 200:
        r_json = json.loads(r.text)
        return float(r_json['data']['price'])

    else:
        raise ExchangeException(message="Invalid request status code {}".format(r.status_code),
                                status_code=r.status_code)


def main():
    toks = get_token_list()
    common = []
    not_common = []
    for tok in toks:
        if tok in tokens.values():
            common.append(tok)
        else:
            not_common.append(tok)
    pp.pprint(common)
    pp.pprint(get_token_price('STAC'))


if __name__ == "__main__":
    main()
