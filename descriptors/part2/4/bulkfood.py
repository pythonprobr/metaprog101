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


class LineItem(object):
    weight = Quantity()
    price = Quantity()

    def __new__(cls, *args, **kwargs):
        for key, attr in cls.__dict__.items():
            if isinstance(attr, Quantity):
                attr.set_name('__' + cls.__name__, key)
        return super(LineItem, cls).__new__(cls, *args, **kwargs)

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
