matrix = [
        [1, 2, 3, 4],
        [3, 4, 5, 6],
        [6, 7, 8, 9],
        [8, 7, 6, 5]
    ]
result = 1

for y in range(len(matrix)):
    for x in range(y):
        value = matrix[y][x]
        result *= value

print(result)
