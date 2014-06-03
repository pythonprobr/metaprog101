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


Verificação de tipos:

    >>> l.append('x')
    Traceback (most recent call last):
      ...
    TypeError: 'x' is not the same type as 3 (int)
    >>> l.extend([10, [11]])
    Traceback (most recent call last):
      ...
    TypeError: '[11]' is not the same type as 3 (int)

"""
