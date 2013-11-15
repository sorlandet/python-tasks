# -*- coding: utf-8 -*-

import sys

# Input format
# В единственной строке располагается число N (0 < N ≤ 105) – полупериод терпения директора в ожидании завершения очередного проекта.
#
# Output format
# Нужно вывести единственное число – количество способов организовать свою работу, чтобы сдать проект ровна через 2N дней.
# Ответ выведите по модулю 10^9+9.
def binPow(x, pow, maxsize):
    ans = 1

    while pow != 0:
        if pow % 2 != 0:
            ans = (ans * x) % maxsize
            pow -= 1

        x = (x * x) % maxsize
        pow /= 2

    return ans


def main(n, maxsize):

    g = lambda x, y: (x * y) % maxsize
    ans = reduce(g, xrange(1, 2*n + 1))

    for i in xrange(1, n + 1):
        ans = (ans * binPow(i, maxsize - 2, maxsize)) % maxsize

    for i in xrange(1, n + 2):
        ans = (ans * binPow(i, maxsize - 2, maxsize)) % maxsize

    return ans




if __name__ == '__main__':
    fo = sys.stdin
    n = long(fo.readline())
    fo.close()
    #n = 84  # 572959526
    mod = 1000000009
    sys.stdout.write('%s' % main(n, mod))



