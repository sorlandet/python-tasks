#Your code here
#You can import some modules or create additional functions


def checkio(data):
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
        ret = []
        for x, line in enumerate(grille):
            for y, cell in enumerate(line):
                if hole in cell:
                    ret.append(template[x][y])
        return ''.join(ret)

    grille, template = map(convert_to_matrix, data)

    val = ''

    for i in range(4):
        val += decrypt(grille, template)
        grille = rotate_90degree(grille)

    return val


#Some hints
#Just loop for iterations
#Maybe you will convert grille for more comfortable view


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
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
