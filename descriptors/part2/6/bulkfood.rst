==============
LineItem tests
==============

A line item for a bulk food order has description, weight and price fields::

	>>> from bulkfood import LineItem
	>>> raisins = LineItem('Golden raisins', 10, 36.95)
	>>> raisins.weight, raisins.description, raisins.price
	(10, 'Golden raisins', 36.95)

The ``weight`` of a ``LineItem`` must be > 0::

	>>> raisins.weight = 0
	Traceback (most recent call last):
		...
	ValueError: value must be > 0

The same rule applies to ``price``::

	>>> raisins.price = 0
	Traceback (most recent call last):
		...
	ValueError: value must be > 0

As before, the descriptive attribute names are used::

	>>> [name for name in dir(raisins) if name[-1] != '_'] #doctest: +ELLIPSIS
	['__LineItem_price', '__LineItem_weight', ..., 'price', 'weight']

Here we have the same funtionality as the previous step, refactored.
``BulkEntityMeta`` and ``Quantity`` are in a new ``entity`` module. And a
class ``BusinessEntity`` is created to serve as the superclass of
``LineItem``, so that the application developer does not need to know about
metaclasses.

    >>> type(raisins)
    <class 'bulkfood.LineItem'>
    >>> LineItem.__bases__
    (<class 'entity.BusinessEntity'>,)
    >>> type(LineItem)
    <class 'entity.BusinessEntityMeta'>

The ``bulkfood`` module *looks* almost as simple as it was in the first step,
but its numeric attributes are now encapsulated by a reusable descriptor class
that validades their values.
