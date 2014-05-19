==============
LineItem tests
==============

A line item for a bulk food order has description, weight and price fields::

    >>> from bulkfood import LineItem
    >>> raisins = LineItem('Golden raisins', 10, 6.95)
    >>> raisins.weight, raisins.description, raisins.price
    (10, 'Golden raisins', 6.95)

A ``subtotal`` method gives the total price for that line item::

    >>> raisins.subtotal()
    69.5

