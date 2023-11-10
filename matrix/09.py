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

for vertical in range(x):
    for horizontal in range(y):
        matrix[horizontal][vertical] = number
        number += 1

for row in matrix:
    print(row)
