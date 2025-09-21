import doctest 
import abc
from tombola import Tombola

# import bingo, lotto, tombolist
TEST_FILE = 'tombola_tests.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'

def main(argv):
    verbose = '-v' in argv
    real_subclasses = Tombola.__subclasses__()
    # ISSUES in virtual_subclasses
    # https://github.com/fluentpython/example-code/issues/24
    virtual_subclasses = [ref() for ref in abc._get_dump(Tombola)[0] if ref()]
    for cls in real_subclasses + virtual_subclasses:
        test(cls, verbose)
        
        
def test(cls, verbose=False):
    res = doctest.testfile(
        TEST_FILE,
        globs={'ConcreteTombola': cls},
        verbose=verbose,
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE
    )
    tag = 'FAIL' if res.failed else 'OK'
    print(TEST_MSG.format(cls.__name__, res, tag))
    
    
if __name__ == '__main__':
    import sys
    main(sys.argv)