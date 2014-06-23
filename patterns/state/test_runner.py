import sys
import importlib
import doctest

TESTS = 'carstereo_tests.txt'

def test(module_cls_name, verbose=False):
    module_name, _, cls_name = module_cls_name.rpartition('.')
    module = importlib.import_module(module_name)

    cls = getattr(module, cls_name)

    res = doctest.testfile(TESTS,
                           globs={cls_name: cls},
                           verbose=verbose,
                           optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    print('{:10} {}'.format(module_name, res))


if __name__ == '__main__':

    args = sys.argv[:]
    if '-v' in args:
        args.remove('-v')
        verbose = True
    else:
        verbose = False

    if len(args) == 2:
        test(args[1], verbose)
    else:
        print('Usage: {} <module.class> [-v]'.format(sys.argv[0]))
