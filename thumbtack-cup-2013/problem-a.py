# -*- coding: utf-8 -*-

import sys

# Input format
# Первая строка входного файла содержит целое число N – количество программистов (1 < N ≤ 105).
# В каждой из следующих N строк записаны через пробел 2 натуральных числа – Bi и Ti (1 ≤ Bi, Ti ≤ 1000),
# где Bi – время в часах от начала работы над проектом, когда i-ый программист совершит первый коммит, Ti – период в часах, с которым i-ый программист делает коммиты в VCS.
# И, наконец, в последней строке записано целое число M – номер юбилейного коммита (1 ≤ M ≤ 1012).
#
# Output format
# В выходной файл следует вывести одно целое число – час от начала работы над проектом (считая с первого), в который будет отправлен юбилейный коммит.
import cStringIO


def main(fo):
    sn = fo.readline()
    n = long(sn)
    goal = 0
    b, t = ([], [])

    while 1:
        lines = fo.readlines(100000)
        if not lines:
            break
        for line in lines:
            l = line.strip()
            try:
                bi, ti = l.split(' ')
                b.append(long(bi))
                t.append(long(ti))
            except ValueError:
                goal = long(l)

    #for line in fo:
    #    l = line.strip()
    #    try:
    #        bi, ti = l.split(' ')
    #        b.append(long(bi))
    #        t.append(long(ti))
    #    except ValueError:
    #        goal = long(l)


    l = 0
    r = sys.maxsize
    while l + 1 != r:
        cnt = 0
        m = (l + r) / 2
        for i in xrange(n):
            if cnt > sys.maxsize:
                break
            if m >= b[i]:
                cnt += (m - b[i]) / t[i] + 1
        if cnt < goal:
            l = m
        else:
            r = m

    return r

if __name__ == '__main__':
    fo = sys.stdin
    #fo = open(sys.argv[1], 'rU')

    sys.stdout.write('%s' % main(fo))

    fo.close()

