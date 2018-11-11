from src.order import Order


class RadarBook:
    def __init__(self, asks=None, bids=None, pair=None):
        self.asks = asks
        self.bids = bids
        self.pair = pair

    def __repr__(self):
        return 'Order book for pair %s' % (self.pair)

    @classmethod
    def load_from_market_pair(cls, marketID, **market_json):
        asks = ([Order(market_json['quoteTokenAddress'],
                       market_json['baseTokenAddress'],
                       'ASK', 'RADAR_RELAY', ask['price'],
                       ask['remainingBaseTokenAmount']) for ask in market_json['asks']])

        bids = ([Order(market_json['quoteTokenAddress'],
                       market_json['baseTokenAddress'],
                       'ASK', 'RADAR_RELAY', bid['price'],
                       bid['remainingQuoteTokenAmount']) for bid in market_json['bids']])

        return cls(asks, bids, marketID)
