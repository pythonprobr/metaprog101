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

However, in this version the linking of the descriptor instances to their
respective attribute names is not done in ``LineItem.__new__`` but in a
*metaclass*. ``LineItem`` is now declared to be an instance of
``BusinessEntityMeta``::

    >>> type(LineItem)
    <class 'bulkfood.BusinessEntityMeta'>

The ``BusinessEntityMeta`` metaclass is responsible for building the
``LineItem`` class, and ``BusinessEntityMeta.__init__`` is the right place
to implement the logic that was previously in ``LineItem.__new__``. That way,
the code linking descriptors and attributes runs only once, when the
``LineItem`` class is defined at module import time.
