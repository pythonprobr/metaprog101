=======
Passo 6
=======

Um pedido de alimentos a granel é uma coleção de ``ItenPedido``.
Cada item possui campos para descrição, peso e preço::

	>>> from granel import ItemPedido
	>>> ervilha = ItemPedido('ervilha partida', 500, 3.95)
	>>> ervilha.descricao, ervilha.peso, ervilha.preco
	('ervilha partida', 500, 3.95)

O peso de um ``ItemPedido`` deve ser maior que zero::

	>>> ervilha.peso = 0
	Traceback (most recent call last):
		...
	ValueError: valor deve ser > 0

A mesma regra se aplica ao preço::

	>>> lentilha = ItemPedido('lentilha', 1000, 0.00)
	Traceback (most recent call last):
		...
	ValueError: valor deve ser > 0

Armazenagem dos valores
=======================

Nesta versão as instâncias dos descritores recebem um nome mais descritivo durante a construção das instâncias de ``ItemPedido``::

	>>> dir(ervilha) # doctest: +ELLIPSIS
	['__ItemPedido_peso', '__ItemPedido_preco', ...]

Implementação
=============

.. literalinclude:: modelo.py
   :linenos:

.. literalinclude:: granel.py
   :linenos:
