def spiral(nbr):
    m = [[0 for n in range(nbr)] for n in range(nbr)]
    direction = 'r'
    x = y = 0
    side = nbr
    for i in range(nbr ** 2):
        m[y][x] = i + 1
        if direction == 'r':
            x += 1
            if x == side-1: direction = 'd'
        elif direction == 'd':
            y += 1
            if y == side-1: direction = 'l'
        elif direction == 'l':
            x -= 1
            if x == nbr-side:
                direction = 'u'
                side -= 1
        elif direction == 'u':
            y -= 1
            if y == nbr-side: direction = 'r'
    return m

for row in spiral(9): print(*row, sep='\t')
