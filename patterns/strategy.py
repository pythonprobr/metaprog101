
"""
    >>> joe = Customer('John Doe', 0)
    >>> ann = Customer('Ann Smith', 1100)
    >>> cart = [LineItem('banana', 3, .5),
    ...         LineItem('apple', 10, 1.5),
    ...         LineItem('watermellon', 5, 5.0)]
    >>> Order(joe, cart, 'fidelity')
    <Order total: 41.50 due: 41.50>
    >>> Order(ann, cart, 'fidelity')
    <Order total: 41.50 due: 39.42>
    >>> banana_cart = [LineItem('banana', 30, .5),
    ...                LineItem('apple', 10, 1.5)]
    >>> Order(joe, banana_cart, 'bulk')
    <Order total: 30.00 due: 28.50>
    >>> long_order = [LineItem(str(code), 1, 1.0) for code in range(10)]
    >>> Order(joe, long_order, 'large_order')
    <Order total: 10.00 due: 9.30>


"""

from abc import ABCMeta, abstractmethod
from collections import namedtuple

import promos

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.__dict__.update(locals())

    @property
    def total(self):
        return self.price * self.quantity


class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = getattr(promos, promotion+'_promo')

    @property
    def total(self):
        try:
            return self.__total
        except AttributeError:
            self.__total = sum(item.quantity * item.price
                               for item in self.cart)
            return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total, self.due())
