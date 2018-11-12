from constants import Exchange, OrderType, tokens


'''TODO: remove radar_tokes, replace with tokens'''

class Order:
    def __init__(self, quote_token, base_token, order_type, exchange, rate, amount):
        self.quote_token = tokens[quote_token]
        self.base_token = tokens[base_token]
        self.order_type = OrderType[order_type]
        self.exchange = Exchange[exchange]
        self.rate = rate
        self.amount = amount

    def __repr__(self):
        if self.order_type == OrderType.BID:
            return '%s order to buy %f %r for %r at exchange rate %f on %s.' \
                   % (self.order_type.value, float(self.amount), self.base_token, self.quote_token, float(self.rate), self.exchange.value)

        if self.order_type == OrderType.ASK:
            return '%s order to sell %f %r for %r at exchange rate %f on %s.' \
                   % (self.order_type.value, float(self.amount), self.base_token, self.quote_token, float(self.rate), self.exchange.value)
