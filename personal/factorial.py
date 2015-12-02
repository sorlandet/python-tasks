import datetime
import sys
import getopt
import timeit

from fn import recur
from guppy import hpy


def fact0(n):
    if n == 0:
        return 1
    return n * fact0(n - 1)


# tail call optimization
def fact1(n, acc=1):
    if n == 0:
        return acc
    return fact1(n - 1, acc * n)


@recur.tco
def fact2(n, acc=1):
    if n == 0:
        return False, acc
    return True, (n - 1, acc * n)


def main(argv):
    n = None

    try:
        opts, args = getopt.getopt(argv, "hn:", ["number="])
    except getopt.GetoptError:
        print 'factorial.py -n <number>'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print 'factorial.py -n <number>'
            sys.exit()
        elif opt in ("-n", "--number"):
            n = int(arg)

    print 'Calculating factorial of:', n, '100k times'

    h = hpy()

    print 'basic'
    print 'time:', timeit.timeit("fact0(%s)" % n, setup="from __main__ import fact0", number=1000000)
    h.setref()
    print 'result:', fact0(n)
    print 'total memory:', h.heap().size, ' bytes'
    print '====================================================================='

    print 'tail call optimized'
    print 'time:', timeit.timeit("fact1(%s)" % n, setup="from __main__ import fact1", number=1000000)
    h.setref()
    print 'result:', fact1(n)
    print 'total memory:', h.heap().size, ' bytes'
    print '====================================================================='

    print 'tail call optimized using fn.py decorator'
    print 'time:', timeit.timeit("fact2(%s)" % n, setup="from __main__ import fact2", number=100000)
    h.setref()
    print 'result:', fact2(n)
    print 'total memory:', h.heap().size, ' bytes'
    print '====================================================================='


if __name__ == '__main__':
    start_time = datetime.datetime.now()

    main(sys.argv[1:])

    end_time = datetime.datetime.now()
    c = end_time - start_time

    print '%d seconds %d microseconds' % (c.seconds, c.microseconds)