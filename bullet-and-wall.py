"""
Input: Four lists with coordinates--each one is a list of x and y coordinates--W1, W2, A, B (Integers).
Output: Whether the bullet hits the wall or not, aka True or False.
"""
from math import fabs
import datetime


# 4 seconds 651000 microseconds
def checkio1(data):

    def in_beam(end, sign, x):
        if sign >= 0.0 and x <= end:
            return True
        elif sign < 0.0 and x >= end:
            return True
        return False

    def in_region(start, end, point):
        sign = end - start
        if sign >= 0.0 and start <= point <= end:
            return True
        elif sign < 0.0 and start >= point >= end:
            return True
        return False

    xw1, yw1 = map(float, data[0])
    xw2, yw2 = map(float, data[1])
    xa, ya = map(float, data[2])
    xb, yb = map(float, data[3])

    x12 = xw1 - xw2
    xab = xa - xb

    y12 = yw1 - yw2
    yab = ya - yb

    wall = xw1 * yw2 - yw1 * xw2
    beam = xa * yb - ya * xb
    c = x12 * yab - y12 * xab

    if fabs(c) < 0.01:
        # No intersection
        if wall != beam:
            return False

        return in_beam(xb, xab, xw2) and in_beam(yb, yab, yw2)
    else:
        # Intersection
        x = (wall * xab - beam * x12) / c
        y = (wall * yab - beam * y12) / c

        is_beam_ok = in_beam(xa, xab, x) and in_beam(ya, yab, y)
        is_wall_ok = in_region(xw1, xw2, x) and in_region(yw1, yw2, y)

        return is_beam_ok and is_wall_ok

# 1 seconds 616000 microseconds
def checkio2(data):

    u1, u2 = data[0]
    v1, v2 = data[1]
    a1, a2 = data[2]
    b1, b2 = data[3]

    c11, c12, c21, c22 = v1 - u1, a1 - b1, v2 - u2, a2 - b2
    d1, d2 = a1 - u1, a2 - u2

    D = 1. * (c11 * c22 - c12 * c21)
    Dx = d1 * c22 - d2 * c12
    Dy = c11 * d2 - c21 * d1

    if D != 0:
        x, y = Dx / D, Dy / D
        return 0 <= x <= 1 and y >= 0

    return Dx == 0 and 1. * d1 / c12 > 0


# 2 seconds 416000 microseconds
def checkio(data):

    def cross_product(v1,v2):
        # return applicate component only
        return v1[0]*v2[1] - v1[1]*v2[0]

    def dot_product(v1,v2):
        return v1[0]*v2[0] + v1[1]*v2[1]

    def between(v, v1, v2):
        prd = cross_product(v1,v2)
        if abs(prd) < 0.000001:
            return dot_product(v, v1) > 0 or dot_product(v, v2) > 0
        else:
            return cross_product(v1,v)*prd >= 0 and cross_product(v,v2)*prd >= 0

    xw1, yw1 = data[0]
    xw2, yw2 = data[1]
    xa, ya = data[2]
    xb, yb = data[3]

    return between((xb-xa,yb-ya), (xw1-xa,yw1-ya), (xw2-xa,yw2-ya))

#Some hints
#You can search intersection point for lines
#Or look to rays geometry


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    start_time = datetime.datetime.now()
    for i in range(100000):
        assert checkio([[0, 1], [1, 2], [2, 0], [0, 2]]) == True, "0st example"
        assert checkio([[0, 0], [0, 2], [5, 1], [3, 1]]) == True, "1st example"
        assert checkio([[0, 0], [0, 2], [3, 1], [5, 1]]) == False, "2nd example"
        assert checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) == True, "3rd example"
        assert checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) == False, "4th example"
        assert checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) == True, "5th example"
        assert checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) == False, "6th example"

    end_time = datetime.datetime.now()
    c = end_time - start_time

    print '%d seconds %d microseconds' % (c.seconds, c.microseconds)
