# -*- coding: utf-8 -*-

import sys


# Input format
# В первой строке расположены три целых числа X, Y, Z (2 ≤ X,Y,Z ≤ 100) - размеры параллелепипеда,
#  При этом одна из вершин совпадает с началом координат, противоположная вершина имеет координаты (X, Y, Z), его стороны параллельны осям координат.
# Во второй строке записаны три целых числа x1, y1, z1 (0 ≤ x1 ≤ X, 0 ≤ y1 ≤ Y, 0 ≤ z1 ≤ Z) - координаты игрока.
# В третьей строке записаны три целых числа x2, y2, z2 (0 ≤ x2 ≤ X, 0 ≤ y2 ≤ Y, 0 ≤ z2 ≤ Z) - координаты флага.
#
# Output format
# Необходимо вывести единственное число - кратчайшее расстояние от игрока до флага по поверхности параллелепипеда. Ответ вывести с точностью не менее 4 точек после запятой.
import math

cos = [1, 0, -1, 0]
sin = [0, 1 ,0, -1]
u = [0, 0, 0, 0, 0, 0]

EPS = 1e-9


def eq(x, y):
    return abs(x - y) < EPS


def dist(x, y):
    return math.sqrt(x**2 + y**2)


def add_min_dist(ans, ps_x, ps_y):
    return min(ans, dist(ps_x - x1, ps_y - y1))


def rotX(ornt, x, y):
    return x * cos[ornt % 4] - y * sin[ornt % 4]


def rotY(ornt, x, y):
    return x * sin[ornt % 4] + y * cos[ornt % 4]


def dfs(v, ornt, cur_x, cur_y, ans):


    if u[v]:
        return ans

    if v == goal:
        if v == 0:
            dx = x2
            dy = y2

        elif v == 2:
            dx = w - x2
            dy = y2

        elif v == 3:
            dx = d - z2
            dy = y2

        else:
            ans = -1  # should not reach here

        return add_min_dist(ans, cur_x + rotX(ornt, dx, dy), cur_y + rotY(ornt, dx, dy))

    u[v] = 1

    if v == 0:
        dfs(1, ornt, cur_x + rotX(ornt, w, 0), cur_y + rotY(ornt, w, 0), ans)
        dfs(3, ornt, cur_x + rotX(ornt, -d, 0), cur_y + rotY(ornt, -d, 0), ans)
        dfs(4, ornt, cur_x + rotX(ornt, 0, h), cur_y + rotY(ornt, 0, h), ans)
        dfs(5, (ornt + 2) % 4, cur_x + rotX(ornt, w, 0), cur_y + rotY(ornt, w, 0), ans)
    elif v == 1:
        dfs(0, ornt, cur_x + rotX(ornt, -w, 0), cur_y + rotY(ornt, -w, 0), ans)
        dfs(2, ornt, cur_x + rotX(ornt, d, 0), cur_y + rotY(ornt, d, 0), ans)
        dfs(4, (ornt + 3) % 4, cur_x + rotX(ornt, 0, h + w), cur_y + rotY(ornt, 0, h + w), ans)
        dfs(5, (ornt + 3) % 4, cur_x, cur_y, ans)
    elif v == 2:
        dfs(1, ornt, cur_x + rotX(ornt, -d, 0), cur_y + rotY(ornt, -d, 0), ans)
        dfs(3, ornt, cur_x + rotX(ornt, w, 0), cur_y + rotY(ornt, w, 0), ans)
        dfs(4, (ornt + 2) % 4, cur_x + rotX(ornt, w, h + d), cur_y + rotY(ornt, w, h + d), ans)
        dfs(5, ornt, cur_x + rotX(ornt, 0, -d), cur_y + rotY(ornt, 0, -d), ans)
    elif v == 3:
        dfs(0, ornt, cur_x + rotX(ornt, d, 0), cur_y + rotY(ornt, d, 0), ans)
        dfs(2, ornt, cur_x + rotX(ornt, -w, 0), cur_y + rotY(ornt, -w, 0), ans)
        dfs(4, (ornt + 1) % 4, cur_x + rotX(ornt, d, h), cur_y + rotY(ornt, d, h), ans)
        dfs(5, (ornt + 1) % 4, cur_x + rotX(ornt, d, -w), cur_y + rotY(ornt, d, -w), ans)
    elif v == 4:
        dfs(0, ornt, cur_x + rotX(ornt, 0, -h), cur_y + rotY(ornt, 0, -h), ans)
        dfs(1, (ornt + 1) % 4, cur_x + rotX(ornt, w + h, 0), cur_y + rotY(ornt, w + h, 0), ans)
        dfs(2, (ornt + 2) % 4, cur_x + rotX(ornt, w, d + h), cur_y + rotY(ornt, w, d + h), ans)
        dfs(3, (ornt + 3) % 4, cur_x + rotX(ornt, -h, d), cur_y + rotY(ornt, -h, d), ans)
    elif v == 5:
        dfs(0, (ornt + 2), cur_x + rotX(ornt, w, 0), cur_y + rotY(ornt, w, 0), ans)
        dfs(1, (ornt + 1) % 4, cur_x + rotX(ornt, 0, 0), cur_y + rotY(ornt, 0, 0), ans)
        dfs(2, (ornt + 0) % 4, cur_x + rotX(ornt, 0, d), cur_y + rotY(ornt, 0, d), ans)
        dfs(3, (ornt + 3) % 4, cur_x + rotX(ornt, w, d), cur_y + rotY(ornt, w, d), ans)

    u[v] = 0


    return ans


def main(fo):
    global w, h, d
    global x1, y1, z1
    global x2, y2, z2
    global goal, u

    w, h, d = [long(n) for n in fo.readline().strip().split(' ')]
    x1, y1, z1 = [long(n) for n in fo.readline().strip().split(' ')]
    x2, y2, z2 = [long(n) for n in fo.readline().strip().split(' ')]

    print w, h, d
    print x1, y1, z1
    print x2, y2, z2

    if eq(x1, w):
        x1 = 0
        x2 = w - x2

    if eq(y1, h):
        y1 = 0
        y2 = h - y2

    if eq(z1, d):
        z1 = 0
        z2 = d - z2

    if eq(x1, 0):
        x1, z1 = z1, x1
        x2, z2 = z2, x2
        w, d = d, w

    if eq(y1, 0):
        y1, z1 = z1, y1
        y2, z2 = z2, y2
        h, d = d, h

    if eq(x2, w):
        x1 = w - x1
        x2 = 0

    if eq(y2, h):
        y1 = h - y1
        y2 = 0

    if eq(y2, 0):
        x1, y1 = y1, x1
        x2, y2 = y2, x2  # now x2 equal to 0
        w, h = h, w

    if eq(z2, 0):
        goal = 0
    elif eq(x2, 0):
        goal = 3
    elif eq(z2, d):
        goal = 2
    else:
        return 1  # shouldn't reach here
    ans = 0

    return dfs(0, 0, 0, 0, ans)

if __name__ == '__main__':
    #fo = sys.stdin
    fo = open('problem-b-input.txt', 'rU')  #1.5159245

    sys.stdout.write('{:.4f}'.format(main(fo)))

    fo.close()

