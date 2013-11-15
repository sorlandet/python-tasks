# -*- coding: utf-8 -*-
from itertools import islice

import sys


# Input format
# В первой строке расположено одно число M – количество слов в словаре (1 ≤ M ≤ 50000).
# Далее в M строках расположено по два слова – неправильное и правильное, длинна каждого слова не превосходит 100.
#  Слова состоят из строчных латинских букв. Каждое неправильное слово встречается не больше одного раза.
# В следующей строке располагается единственное число N – количество слов в строке, которую надо исправить (1 ≤ N ≤ 50000).
# В последней строке расположена строка, состоящая из N слов, разделенных пробелами.
#
# Output format
# Необходимо вывести исправленную с помощью словаря строку.
def main(fo):
    d, res, i = ({}, [], 1)
    m = long(fo.readline())

    for line in islice(fo, m + 2):
        l = line.strip()

        if i < m + 1:
            key, val = l.split(' ')
            d.setdefault(key, val)

        if i == m + 1:
            n = long(l)
        if i == m + 2:
            words = l.split(" ")

        i += 1

    for i in xrange(len(words)):
        replacement = d.get(words[i])
        if replacement:
            res.append(replacement)
        else:
            res.append(words[i])
        res.append(' ')

    return ''.join(res)

if __name__ == '__main__':
    fo = sys.stdin
    #fo = open(sys.argv[1], 'rU')  # 'segodnya mama myla ramu '

    sys.stdout.write('%s' % main(fo))

    fo.close()

