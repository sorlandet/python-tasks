import datetime
import random
import sys
import getopt
import timeit
import math
import re


# time: 0.728382110596
def is_prime0(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


# time: 2.27445912361
def is_prime1(n):
    i = 2
    j = 0
    while i**2 <= n and j != 1:
        if n % i == 0:
            j = 1
        i += 1
    if j == 1:
        return False
    else:
        return True


# extremely slow on big numbers
def is_prime2(n):
    """
    Wilson's theorem
    """
    if (math.factorial(n - 1) + 1) % n != 0:
        return False
    else:
        return True


def fermat_primality_test(a, n):
    """
    Fermat primality test
    """

    if a**(n - 1) % n == 1:
        return True
    else:
        return False


def to_binary(n):
    r = []
    while n > 0:
        r.append(n % 2)
        n /= 2
    return r


def miller_rabin_primality_test(n, s=50):
    for j in xrange(1, s + 1):
        a = random.randint(1, n - 1)
        b = to_binary(n - 1)
        d = 1
        for i in xrange(len(b) - 1, -1, -1):
            x = d
            d = (d * d) % n
            if d == 1 and x != 1 and x != n - 1:
                return False
            if b[i] == 1:
                d = (d * a) % n
                if d != 1:
                    return False
                return True


# slow on big numbers
def is_prime_by_regexp(n):
    s = u''.join('1' for i in xrange(n))
    p = re.compile(ur'^1?$|^(11+?)\1+$')
    if re.match(p, s):
        return False
    return True


def get_prime_numbers(start, end):
    for idx in range(start, end):
        if is_prime0(idx):
            yield idx


def main(argv):
    n = None
    start = None

    try:
        opts, args = getopt.getopt(argv, "hn:s:", ['number=', 'start='])
    except getopt.GetoptError:
        print 'get-prime-numbers.py -n <number> -s <start>'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print 'get-prime-numbers.py -n <number> -s <start>'
            sys.exit()
        elif opt in ("-n", "--number"):
            n = int(arg)
        elif opt in ("-s", "--start"):
            start = int(arg)

    if n and start:
        print 'Calculating prime numbers from %d to %d' % (start, n)
        print 'found:',  [el for el in get_prime_numbers(start, n)]
        print '====================================================================='
        sys.exit(2)

    print 'is_prime0'
    print 'time:', timeit.timeit("is_prime0(%s)" % n,
                                 setup="from __main__ import is_prime0", number=100)
    print 'result:', is_prime0(n)
    print '====================================================================='

    print 'is_prime1'
    print 'time:', timeit.timeit("is_prime1(%s)" % n,
                                 setup="from __main__ import is_prime1", number=100)
    print 'result:', is_prime1(n)
    print '====================================================================='

    print 'Wilson''s theorem'
    print 'time:', timeit.timeit("is_prime2(%s)" % n,
                                 setup="from __main__ import is_prime2", number=100)
    print 'result:', is_prime2(n)
    print '====================================================================='

    print 'Fermat primality test'
    print 'time:', timeit.timeit("fermat_primality_test(2, %s)" % n,
                                 setup="from __main__ import fermat_primality_test", number=100)
    print 'result:', fermat_primality_test(2, n)
    print '====================================================================='

    print 'Miller-Rabin primality test'
    print 'time:', timeit.timeit("miller_rabin_primality_test(%s)" % n,
                                 setup="from __main__ import miller_rabin_primality_test", number=100)
    print 'result:', miller_rabin_primality_test(n)
    print '====================================================================='

    print 'is_prime_by_regexp'
    print 'time:', timeit.timeit("is_prime_by_regexp(%s)" % n,
                                 setup="from __main__ import is_prime_by_regexp", number=100)
    print 'result:', is_prime_by_regexp(n)
    print '====================================================================='


if __name__ == '__main__':
    start_time = datetime.datetime.now()

    main(sys.argv[1:])

    end_time = datetime.datetime.now()
    c = end_time - start_time

    print '%d seconds %d microseconds' % (c.seconds, c.microseconds)