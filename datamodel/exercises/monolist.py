# coding: utf-8

"""

Operações básicas:

    >>> l = MonoList()
    >>> l.append(3)
    >>> len(l)
    1
    >>> l
    MonoList([3])
    >>> l.extend(range(4))
    >>> len(l)
    5
    >>> l
    MonoList([3, 0, 1, 2, 3])
    >>> l2 = MonoList('ABC')
    >>> l2
    MonoList(['A', 'B', 'C'])



Verificação de tipos:

    >>> l.append('x')  # doctest: -SKIP
    Traceback (most recent call last):
      ...
    TypeError: 'x' (str) is not the same type as 3 (int)
    >>> l.extend([10, [11]])  # doctest: -SKIP
    Traceback (most recent call last):
      ...
    TypeError: [11] (list) is not the same type as 3 (int)
    >>> len(l)
    5
    >>> MonoList(['A', 0])
    Traceback (most recent call last):
      ...
    TypeError: 0 (int) is not the same type as 'A' (str)



"""

import UserList


class MonoList(UserList.UserList):

    def __init__(self, data=None):
        super(MonoList, self).__init__()
        if data:
            self._item_type = type(data[0])

    def append(self, item):
        self._check_type(item)
        self.data.append(item)

    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self.data)

    def _check_type(self, item):
        if self.data:
            first = self.data[0]
            if type(first) is not type(item):
                msg = '%r (%s) is not the same type as %r (%s)'
                raise TypeError(msg % (item, type(item).__name__,
                                   first, type(first).__name__))


    def extend(self, iterable):
        new_items = []
        for item in iterable:
            self._check_type(item)
            new_items.append(item)
        self.data.extend(new_items)













