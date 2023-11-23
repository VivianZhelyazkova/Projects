matrix = [
        [1, 2, 3, 4],
        [3, 4, 5, 6],
        [6, 7, 8, 9],
        [8, 7, 6, 5]
    ]
is_negative = False

for y in range(len(matrix)):
    for x in range(len(matrix[y]) - (y+1)):
        if matrix[y][x] < 0:
            is_negative = True

print(is_negative)


