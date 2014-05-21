==================================
Benchmark simples dos exemplos
==================================

Criando 100 000 instâncias em cada passo/exemplo.

===== ===== ============ ==========================================================
passo tempo instancias/s descrição
===== ===== ============ ==========================================================
  1   0.072     1388152  sem validação
  2   0.104      962937  validação de 1 atributo via property
  3   0.175      572846  validação de 2 atributos via descriptors
  4   1.338       74756  descriptors configurados em ``ItemPedido.__new__``
  5   0.179      557603  descriptors configurados na metaclasse de ``ItemPedido``
 5d   0.183      546265  descriptors configurados em decorator sobre ``ItemPedido``
  6   0.185      539266  como 5, com descriptor e metaclasse em outro módulo
 6d   0.189      529871  como 5d, com descriptor e decorator em outro módulo
===== ===== ============ ==========================================================

As versões de 3 a 6 são equivalentes em funcionalidade: a validação é feita nos atributos ``peso`` e ``preco``. Na versão 2 apenas o ``peso`` é validado e na versão 1 não há validação.

Este benchmark é limitado pois a única operação feita é instanciação. Em um programa real, uma vez instanciados os objetos sofrem outras operações, o que significa que o custo da instanciação é mais diluído. 

Em outras palavras: neste benchmark a versão 1 é 2.4 vezes mais rápida que a versão 3, mas isso não significa que um programa real sem validação será 2.4 vezes mais rápido que um que usa validação de atributos por descriptors.
