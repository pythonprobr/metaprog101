"""
Classic implementation of the Strategy pattern
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
