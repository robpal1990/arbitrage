import requests
import json
from src.constants import tokens

ORDERBOOK_ENDPOINT = 'https://api.radarrelay.com/v2/markets/{marketID}/book'
marketID = 'ZRX-WETH'





def main():
    URL = ORDERBOOK_ENDPOINT.format(
        marketID=marketID
    )
    r = requests.get(URL)
    book = json.loads(r.text)
    print book.keys()
    print tokens[book['quoteTokenAddress']], tokens[book['baseTokenAddress']]
    print map(lambda x: x['price'], book['bids'])
    print map(lambda x: x['price'], book['asks'])
    # pp.pprint(book)


if __name__ == '__main__':
    main()