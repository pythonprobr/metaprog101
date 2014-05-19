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

In order to store the ``Quantity`` values with better names in the
``LineItem`` instances, a ``__new__`` method is added to provide the
attribute naming logic. The new attribute names include the name of the
actual class attribute to which each descriptor is bound, ``weight`` and
``price``::

	>>> [name for name in dir(raisins) if name[-1] != '_'] #doctest: +ELLIPSIS
	['__LineItem_price', '__LineItem_weight', ..., 'price', 'weight']

The reason for doing the attribute naming in a ``__new__`` method and not in
the ``__init__`` is that ``__new__`` is called before ``__init__`` to
actuually build a new instance, which is then initialized by ``__init__``.
Conceptually, the linking of the descriptors to their attribute names is
part of the building stage.

That way, when ``__init__`` runs the descriptors are properly configured and
the initialization remains straightforward: nothing has changed in the body
of ``LineItem.__init__`` since the first step of this demonstration::

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

The problem with this approach
==============================

This approach works, but it is not optimal: the linking of descriptors to
instance attribute names is done every time a new ``LineItem`` instance is
created, but the binding of descriptors to class attributes is done at class
definition time, that is, only once. A better implementation would do the
name linking at import time, when the ``LineItem`` class is defined.

In order to interfere with the class creation process, we need to create a
*metaclass*. A metaclass is a class whose instances are classes; in other
words, a class designed to build other classes.

By default, new-style classes in Python are instances of the ``type``
metaclass::

    >>> type(LineItem)
    <type 'type'>

This means that the ``LineItem`` class is built by ``type``.

Since we want to interfere with the construction of ``LineItem``, we need
to create a our own metaclass. That is the next step.
