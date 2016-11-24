"""
https://api.itbit.com/docs
"""

# Import Built-Ins
import logging

# Import Third-Party

# Import Homebrew
from bitex.api.rest import ItbitREST
from bitex.utils import return_json

# Init Logging Facilities
log = logging.getLogger(__name__)


class ItBit(ItbitREST):
    def __init__(self, key='', secret='', key_file=''):
        super(ItbitREST, self).__init__(key, secret)
        if key_file:
            self.load_key(key_file)

    def public_query(self, endpoint, **kwargs):
        return self.query('GET', 'markets/' + endpoint, **kwargs)

    def private_query(self, endpoint, **kwargs):
        return self.query('POST', endpoint, authenticate=True, **kwargs)

    """
    BitEx Standardized Methods
    """

    @return_json(None)
    def ticker(self, pair):
        return self.public_query('%s/ticker' % pair, params={'pair': pair})

    @return_json(None)
    def order_book(self, pair):
        return self.public_query('%s/order_book' % pair, params={'pair': pair})

    @return_json(None)
    def trades(self, pair, **kwargs):
        q = {'pair': pair}
        q.update(kwargs)
        return self.public_query('%s/trades' % pair, params=q)

    @return_json(None)
    def bid(self, pair, price, amount, **kwargs):
        raise NotImplementedError()

    @return_json(None)
    def ask(self, pair, price, amount, **kwargs):
        raise NotImplementedError()

    @return_json(None)
    def cancel_order(self, order_id, all=False, **kwargs):
        raise NotImplementedError()

    @return_json(None)
    def order(self, order_id, **kwargs):
        raise NotImplementedError()

    @return_json(None)
    def balance(self, **kwargs):
        raise NotImplementedError()

    @return_json(None)
    def withdraw(self, _type, source_wallet, amount, tar_addr, **kwargs):
        raise NotImplementedError()

    @return_json(None)
    def deposit_address(self, **kwargs):
        raise NotImplementedError()

    """
    Exchange Specific Methods
    """