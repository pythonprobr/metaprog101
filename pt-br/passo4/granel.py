class Quantidade(object):

    def __init__(self):
        self.set_nome(self.__class__.__name__, id(self))

    def set_nome(self, prefix, key):
        self.nome_alvo = '%s_%s' % (prefix, key)

    def __get__(self, instance, owner):
        return getattr(instance, self.nome_alvo)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.nome_alvo, value)
        else:
            raise ValueError('valor deve ser > 0')


class ItemPedido(object):
    peso = Quantidade()
    preco = Quantidade()

    def __new__(cls, *args, **kwargs):
        for chave, atr in cls.__dict__.items():
            if hasattr(atr, 'set_nome'):
                atr.set_nome('__' + cls.__name__, chave)
        return super(ItemPedido, cls).__new__(cls, *args, **kwargs)

    def __init__(self, descricao, peso, preco):
        self.descricao = descricao
        self.peso = peso
        self.preco = preco

    def subtotal(self):
        return self.peso * self.preco
