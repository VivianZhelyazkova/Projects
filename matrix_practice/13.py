matrix = [
    ['', '', '', '', '', 'x',  '', ''],
    ['', '', '', '', '', 'x', '', ''],
    ['', '', '', '', '', 'x', '', ''],
    ['', '', '', '', '', 'x',  '', ''],
    ['', '', '', '', 'x','', 'x', ''],
    ['', '', '', '', 'x', '', '', ''],
    ['', '', '', '', 'x', 'x','x',''],
    ['', '', '', '', '',  'x', '', ''],
]

# spawn coordinates
x = 4
y = 2


def spawn(h, v):
    if h < 0 or h >= len(matrix[0]):
        return
    if v < 0 or v >= len(matrix):
        return
    if matrix[h][v] == "x":
        return
    if matrix[h][v] == "O":
        return
    matrix[h][v] = "O"
    spawn(h + 1, v)  # Right
    spawn(h - 1, v)  # Left
    spawn(h, v - 1)  # Top
    spawn(h, v + 1)  # Bottom


spawn(x, y)

for row in matrix:
    print(row)
