x = int(input())
y = int(input())

number = 1
matrix = []

for column in range(y):
    rows = []
    for row in range(x):
        rows.append(number)
        number += 1
    matrix.append(rows)

print(matrix)

for row in matrix:
    print(row)

