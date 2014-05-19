class Quantity(object):

    def __init__(self):
        self.set_name(self.__class__.__name__, id(self))

    def set_name(self, prefix, key):
        self.attr_name = '%s_%s' % (prefix, key)

    def __get__(self, instance, owner):
        return getattr(instance, self.attr_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.attr_name, value)
        else:
            raise ValueError('value must be > 0')


class BusinessEntityMeta(type):

    def __init__(mcs, name, bases, dict_):
        super(BusinessEntityMeta, mcs).__init__(name, bases, dict_)
        for key, attr in dict_.items():
            if isinstance(attr, Quantity):
                attr.set_name('__' + name, key)


class LineItem(object):
    __metaclass__ = BusinessEntityMeta

    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
