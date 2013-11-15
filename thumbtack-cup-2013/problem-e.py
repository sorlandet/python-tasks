# -*- coding: utf-8 -*-
import sys
import math

# Input format
# В первой строке располагается одно число N (0 < N ≤ 100) - количество полос с разным покрытием.
# В следующей строке располагается N чисел yi - координаты верхнего края i-ой полосы (0 < yi ≤ W), yn = W (W < 3000).
# В следующей строке располагается N чисел vi - скорость движения машинке по i-му покрытию (0 < vi ≤ 100).
# В последней строке располагается два числа Xn и Xk - координаты старта и финиша соответственно. (0 ≤ Xn, Xk ≤ 500)
#
# Output format
# Выведите единственное число - минимальное время, за которое машинка может добраться из точки (Xn, 0) в точку (Xk, W).
# Ответ выведите с точностью до 10-3.


EPS = 1e-3


def distance(x, y):
    return math.sqrt(x**2 + y**2)


def ts(pos, n, xi, yi, vi, xb, xe):
    if pos == n - 1:
        return distance(yi[n - 1] - yi[n - 2], xe - xi[n - 2]) / vi[n - 1]

    l = xb if pos == 0 else xi[pos - 1]
    r = xe

    flag = True

    if l > r:
        tmp = l
        l = r
        r = tmp

    while r - l >= EPS or flag:
        m1 = l + (r - l) / 3.0
        m2 = r - (r - l) / 3.0

        xi[pos] = m1
        delta = distance(yi[0], m1 - xb) if pos == 0 else distance(yi[pos] - yi[pos - 1], m1 - xi[pos - 1])
        t1 = ts(pos + 1, n, xi, yi, vi, xb, xe) + delta / vi[pos]

        xi[pos] = m2
        delta = distance(yi[0], m2 - xb) if pos == 0 else distance(yi[pos] - yi[pos - 1], m2 - xi[pos - 1])
        t2 = ts(pos + 1, n, xi, yi, vi, xb, xe) + delta / vi[pos]

        if t1 < t2:
            r = m2
        else:
            l = m1

        flag = False

    return t1


def main(fo):
    n = long(fo.readline())
    yi = [float(y) for y in fo.readline().strip().split(' ')]
    vi = [float(v) for v in fo.readline().strip().split(' ')]
    xb, xe = [float(x) for x in fo.readline().strip().split(' ')]
    xi = [0 for i in xrange(n)]

    #print yi, vi, xb, xe, xi

    return ts(0, n, xi, yi, vi, xb, xe)

if __name__ == '__main__':
    fo = sys.stdin
    #fo = open('problem-e-input.txt', 'rU')  #1.5159245

    sys.stdout.write('{:.7f}'.format(main(fo)))

    fo.close()

