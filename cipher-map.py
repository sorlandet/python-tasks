#Your code here
#You can import some modules or create additional functions
import datetime

# 15 seconds 838000 microseconds
def checkio1(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.

    def rotate_90degree(matrix):
        size = len(matrix)
        for r in range(size):
            for c in range(r, size):
                x = matrix[r][c]
                y = matrix[c][r]
                matrix[r][c] = y
                matrix[c][r] = x

        for i, r in enumerate(matrix):
            matrix[i] = list(reversed(r))
        return matrix

    def convert_to_matrix(data):
        size = len(data)
        matrix = [[0]*size for i in range(size)]
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                matrix[i][j] = col
        return matrix

    def decrypt(grille, template, hole='X'):
        ret = ''
        for x, line in enumerate(grille):
            for y, cell in enumerate(line):
                if hole in cell:
                    ret += template[x][y]
        return ret

    grille, template = map(convert_to_matrix, data)

    val = ''

    for i in range(4):
        val += decrypt(grille, template)
        grille = rotate_90degree(grille)

    return val


# 4 seconds 995000 microseconds
def checkio2(data):

    def turn(grid):
        return [(j, 3 - i) for i, j in grid]

    def merge(grid, template):
        return ''.join(template[i][j] for i, j in sorted(grid))

    grille, template = data
    grid = [(i, j) for i, line in enumerate(grille)
            for j, sign in enumerate(line) if sign == 'X']
    res = [merge(grid, template)]
    for i in xrange(3):
        grid = turn(grid)
        res.append(merge(grid, template))

    return ''.join(res)


# 5 seconds 353000 microseconds
def checkio(data):

    def transform(matrix):
        return sorted([(3-item[1],item[0]) for item in matrix], key=lambda item: item[1]*4+item[0])

    def decode(grille, matrix):
        str = ''
        for hole in matrix:
            str += grille[hole[1]][hole[0]]
        return str

    grille, template = data
    matrix = []
    str = ''
    for y in range(0,4):
        for x in range(0,4):
            if grille[y][x] == 'X':
                matrix.append((x,y))

    for i in range(0,4):
        str += decode(template, matrix)
        matrix = transform(matrix)
    return str

#Some hints
#Just loop for iterations
#Maybe you will convert grille for more comfortable view


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    start_time = datetime.datetime.now()
    for i in range(100000):

        assert checkio([
            ['X...',
             '..X.',
             'X..X',
             '....'],
            ['itdf',
             'gdce',
             'aton',
             'qrdi']]) == 'icantforgetiddqd', 'First example'

        assert checkio([
            ['....',
             'X..X',
             '.X..',
             '...X'],
            ['xhwc',
             'rsqx',
             'xqzz',
             'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second example'

    end_time = datetime.datetime.now()
    c = end_time - start_time

    print '%d seconds %d microseconds' % (c.seconds, c.microseconds)