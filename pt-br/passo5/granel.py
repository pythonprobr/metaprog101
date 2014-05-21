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


class ModeloMeta(type):

    def __init__(cls, nome, bases, dic):
        super(ModeloMeta, cls).__init__(nome, bases, dic)
        for chave, atr in dic.items():
            if hasattr(atr, 'set_nome'):
                atr.set_nome('__' + nome, chave)


class ItemPedido(object):
    __metaclass__ = ModeloMeta

    peso = Quantidade()
    preco = Quantidade()

    def __init__(self, descricao, peso, preco):
        self.descricao = descricao
        self.peso = peso
        self.preco = preco

    def subtotal(self):
        return self.peso * self.preco
