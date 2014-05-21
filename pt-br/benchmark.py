# coding: utf-8

import sys
from timeit import timeit
from glob import glob

REPEAT = 10**5
CMD = '''ItemPedido('gergelim', 250, 5.30)'''
SETUP = '''from %s.granel import ItemPedido'''

print 'Criando %s instâncias em cada passo' % REPEAT
print
print '=====  =====  ============'
print 'passo  tempo  instancias/s'
print '=====  =====  ============'
for i, subdir in enumerate(glob('passo*'), 1):
    t = timeit(CMD, SETUP % subdir, number=REPEAT)
    print '%3s    %.3f %11d' % (subdir[5:], t, REPEAT/t)
    sys.path.pop()
print '=====  =====  ============'
