import datetime
import sys
import getopt
import timeit

from fn import recur
from guppy import hpy


# The Fibonacci sequence is another classic recursion example
def fib1(n):
    """ Fib with recursion. """
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return fib1(n - 1) + fib1(n - 2)


# In Python, a more efficient version that does not use recursion is
def fib2(n):
    """ Fib without recursion. """
    a, b = 0, 1
    for i in range(1, n + 1):
        a, b = b, a + b
    return b


# Use of cache to speed up the recursive version.
# Note biding of the (mutable) dictionary as a default at run-time.
def fib3(n, cache={0: 1, 1: 1}):
    """
    Fib with recursion and caching.
    :param cache:
    """

    try:
        return cache[n]
    except KeyError:
        cache[n] = fib3(n-1) + fib3(n-2)
        return cache[n]


def main(argv):
    n = None

    try:
        opts, args = getopt.getopt(argv, "hn:", ["number="])
    except getopt.GetoptError:
        print 'fibonacci.py -n <number>'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print 'fibonacci.py -n <number>'
            sys.exit()
        elif opt in ("-n", "--number"):
            n = int(arg)

    print 'Calculating fibonacci of:', n, '100k times'

    h = hpy()

    print 'Fib with recursion'
    print 'time:', timeit.timeit("fib1(%s)" % n, setup="from __main__ import fib1", number=1000000)
    h.setref()
    print 'result:', fib1(n)
    print 'total memory:', h.heap().size, ' bytes'
    print '====================================================================='

    print 'Fib without recursion'
    print 'time:', timeit.timeit("fib2(%s)" % n, setup="from __main__ import fib2", number=1000000)
    h.setref()
    print 'result:', fib2(n)
    print 'total memory:', h.heap().size, ' bytes'
    print '====================================================================='

    print 'Fib with cache recursion'
    print 'time:', timeit.timeit("fib3(%s)" % n, setup="from __main__ import fib3", number=100000)
    h.setref()
    print 'result:', fib3(n)
    print 'total memory:', h.heap().size, ' bytes'
    print '====================================================================='


if __name__ == '__main__':
    start_time = datetime.datetime.now()

    main(sys.argv[1:])

    end_time = datetime.datetime.now()
    c = end_time - start_time

    print '%d seconds %d microseconds' % (c.seconds, c.microseconds)