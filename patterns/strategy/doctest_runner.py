import sys
import importlib
import doctest

def test(doctest_filename, module_cls_name, verbose=False):
    module_name, _, cls_name = module_cls_name.rpartition('.')
    module = importlib.import_module(module_name)

    cls = getattr(module, cls_name)

    res = doctest.testfile(doctest_filename,
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

    if len(args) == 3:
        test(args[1], args[2], verbose)
    else:
        print('Usage: {} <doctest-file> <module.class> [-v]'.format(sys.argv[0]))
