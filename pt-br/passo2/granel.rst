=======
Passo 2
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

Implementação
=============

.. literalinclude:: granel.py
   :linenos:
