import datetime

from toolz import compose, frequencies, partial, curry


def stem(word):
    """ Stem word to primitive form """
    return word.lower().rstrip(",.!:;'-\"").lstrip("'\"")

if __name__ == '__main__':
    start_time = datetime.datetime.now()

    wordcount1 = compose(frequencies, partial(map, stem), str.split)

    print 'partial:', wordcount1("aa bb cc aa bb")

    map = curry(map)

    wordcount2 = compose(frequencies, map(stem), str.split)

    print 'curry:', wordcount2("aa bb cc aa bb")

    end_time = datetime.datetime.now()
    c = end_time - start_time

    print '%d seconds %d microseconds' % (c.seconds, c.microseconds)