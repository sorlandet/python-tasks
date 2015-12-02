import datetime

from toolz import frequencies, compose, concat, merge_with, map


def stem(word):
    """ Stem word to primitive form
        stem("Hello!")
        'hello'
    """
    return word.lower().rstrip(",.!)-*_?:;$'-\"").lstrip("-*'\"(_$'")

wordcount = compose(frequencies, map(stem), concat, map(str.split), open)

if __name__ == '__main__':
    start_time = datetime.datetime.now()

    # Filenames for thousands of books from which we'd like to count words
    filenames = ['book_%d.txt' % i for i in range(1)]

    # Start with sequential map for development
    pmap = map

    # Advance to Multiprocessing map for heavy computation on single machine
    # from multiprocessing import Pool
    # p = Pool(8)
    # pmap = p.map

    # Finish with distributed parallel map for big data
    # from IPython.parallel import Client
    # p = Client()[:]
    # pmap = p.map_sync

    total = merge_with(sum, pmap(wordcount, filenames))

    print 'total:', total

    end_time = datetime.datetime.now()
    c = end_time - start_time

    print '%d seconds %d microseconds' % (c.seconds, c.microseconds)