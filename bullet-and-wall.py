"""
Input: Four lists with coordinates--each one is a list of x and y coordinates--W1, W2, A, B (Integers).
Output: Whether the bullet hits the wall or not, aka True or False.
"""
from math import fabs


def checkio(data):

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

#Some hints
#You can search intersection point for lines
#Or look to rays geometry


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 1], [1, 2], [2, 0], [0, 2]]) == True, "0st example"
    assert checkio([[0, 0], [0, 2], [5, 1], [3, 1]]) == True, "1st example"
    assert checkio([[0, 0], [0, 2], [3, 1], [5, 1]]) == False, "2nd example"
    assert checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) == True, "3rd example"
    assert checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) == False, "4th example"
    assert checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) == True, "5th example"
    assert checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) == False, "6th example"
