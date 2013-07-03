import itertools


def checkio(data):
    vector = []
    for solution in itertools.permutations(data):
        l, r = [], []
        for el in solution:
            if sum(l) > sum(r):
                r.append(el)
            else:
                l.append(el)
        vector.append(int(abs(sum(l)-sum(r))))
    return min(vector)

#Some hints
#Your can use combinations if you want use bruteforce


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
