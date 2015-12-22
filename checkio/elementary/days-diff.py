from datetime import date
from math import fabs


def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    timedelta = date(*date2) - date(*date1)

    return fabs(timedelta.days)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
