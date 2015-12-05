import sys
import getopt
import random

from profilehooks import timecall

sys.setrecursionlimit(10000)


@timecall(immediate=False)
def bubble_sort(seq):
    for passnum in range(len(seq)-1, 0, -1):
        for i in range(passnum):
            if seq[i] > seq[i + 1]:
                seq[i + 1], seq[i] = seq[i], seq[i + 1]
                # temp = seq[i]
                # seq[i] = seq[i + 1]
                # seq[i + 1] = temp
    return seq


@timecall(immediate=False)
def selection_sort(seq):
    """
    The selection sort improves on the bubble sort by making only one exchange for every pass through the list.
    O(n2)
    :param seq:
    :return:
    """
    for fillslot in range(len(seq)-1, 0, -1):
        position_of_max = 0
        for location in range(1, fillslot + 1):
            if seq[location] > seq[position_of_max]:
                position_of_max = location

        temp = seq[fillslot]
        seq[fillslot] = seq[position_of_max]
        seq[position_of_max] = temp
    return seq


@timecall(immediate=False)
def insertion_sort(seq):
    """
    Implementation of the insertion sort
    O(n2)
    :param seq:
    :return:
    """
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j - 1] > seq[j]:
            seq[j - 1], seq[j] = seq[j], seq[j - 1]
            j -= 1
    return seq


@timecall(immediate=False)
def merge_sort(seq):
    """
    Implementation of the merge sort (divide and conquer strategy)
    Merge sort is a recursive algorithm that continually splits a list in half.
    A merge sort is an O(n log n) algorithm.
    :param seq:
    :return:
    """
    if len(seq) > 1:
        mid = len(seq) // 2
        left_half = seq[:mid]
        right_half = seq[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                seq[k] = left_half[i]
                i += 1
            else:
                seq[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            seq[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            seq[k] = right_half[j]
            j += 1
            k += 1
    return seq


# @timecall(immediate=False)
def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        return quick_sort([x for x in seq[1:] if x < seq[0]]) + [seq[0]] + quick_sort([x for x in seq[1:] if x >= seq[0]])


@timecall()
def generate_random_list(n):
    return random.sample(range(10000), n)


def main(argv):
    n = None

    try:
        opts, args = getopt.getopt(argv, "hn:", ["number="])
    except getopt.GetoptError:
        print 'sortings.py -n <number>'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print 'sortings.py -n <number>'
            sys.exit()
        elif opt in ("-n", "--number"):
            n = int(arg)

    print 'Generating random list of numbers'

    random_numbers = generate_random_list(n)

    # print random_numbers

    # bubble_sort(random_numbers)
    # selection_sort(random_numbers)
    insertion_sort(random_numbers)
    merge_sort(random_numbers)
    quick_sort(random_numbers)


if __name__ == '__main__':
    main(sys.argv[1:])