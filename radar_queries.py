import requests
import json


ORDERBOOK_ENDPOINT = 'GET https://api.radarrelay.com/v2/markets/{}/book'
marketID = 'ZRX-WETH'


def main():
    requests.post(ORDERBOOK_ENDPOINT, marketID)
    print 'hehe'
    print 'Dupa'


if __name__ == '__main__':
    main()