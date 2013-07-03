FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):

    def digit(number):
        return FIRST_TEN[int(number)]

    def double_digit(number):
        fd, sd = number
        if fd == '1':
            return SECOND_TEN[int(sd)]

        tens = OTHER_TENS[int(fd) - 2]

        if sd == '0':
            return tens

        return '%s %s' % (tens, digit(sd))

    def tree_digit(number):
        h, fd, sd = number

        hundreds = '%s %s' % (digit(h), HUNDRED)

        if fd == '0' and sd == '0':
            return hundreds

        if fd == '0':
            return '%s %s' % (hundreds, digit(sd))

        return '%s %s' % (hundreds, double_digit(number[1:]))

    cnum = '%d' % number
    s = len(cnum)
    ret = ''

    if s == 1:
        ret = digit(cnum)
    elif s == 2:
        ret = double_digit(cnum)
    elif s == 3:
        ret = tree_digit(cnum)
    return ret

#Some hints
#Don't forget strip whitespaces at the end of string


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert checkio(88) == 'eighty eight', "7th example"
    assert checkio(20) == 'twenty', "8th example"
    assert checkio(100) == 'one hundred', "9th example"
    assert checkio(940) == 'nine hundred forty', "10th example"

