x = int(input())
y = int(input())
matrix = []
number = 1
for column in range(y):
    rows = []
    for row in range(x):
        rows.append(0)
    matrix.append(rows)

number = 1

for horizontal in range(x):
    if horizontal % 2 == 0:
        for vertical in range(y):
            matrix[vertical][horizontal] = number
            number += 1
    else:
        for vertical in range(y - 1, -1, -1):
            matrix[vertical][horizontal] = number
            number += 1

for row in matrix:
    print(row)
