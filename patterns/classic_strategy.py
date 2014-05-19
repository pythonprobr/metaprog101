
"""
    >>> joe = Customer('John Doe', 0)
    >>> ann = Customer('Ann Smith', 1100)
    >>> cart = [LineItem('banana', 3, .5),
    ...         LineItem('apple', 10, 1.5),
    ...         LineItem('watermellon', 5, 5.0)]
    >>> Order(joe, cart, FidelityPromo())
    <Order total: 41.50 due: 41.50>
    >>> Order(ann, cart, FidelityPromo())
    <Order total: 41.50 due: 39.42>
    >>> banana_cart = [LineItem('banana', 30, .5),
    ...                LineItem('apple', 10, 1.5)]
    >>> Order(joe, banana_cart, BulkPromo())
    <Order total: 30.00 due: 28.50>
    >>> long_order = [LineItem(str(code), 1, 1.0) for code in range(10)]
    >>> Order(joe, long_order, LargeOrderPromo())
    <Order total: 10.00 due: 9.30>


"""

from abc import ABCMeta, abstractmethod
from collections import namedtuple

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
        self.promotion = promotion

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
            discount = self.promotion.compute_discount(self)
        return self.total - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total, self.due())


class Promotion(metaclass=ABCMeta):

    @abstractmethod
    def compute_discount(self, order):
        """Return discount as an absolute dollar amount"""


class FidelityPromo(Promotion):
    """5% discount for customers with 1000 or more fidelity points"""

    def compute_discount(self, order):
        return order.total * .05 if order.customer.fidelity >= 1000 else 0


class BulkPromo(Promotion):
    """10% discount for each LineItem with 20 or more units"""

    def compute_discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total * .1
        return discount


class LargeOrderPromo(Promotion):
    """7% discount for orders with 10 or more distinct items"""

    def compute_discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total * .07
