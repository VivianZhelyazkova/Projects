number = int(input())
matrix = []
counter = 0

for y in range(1, number + 1):
    rows = []
    while counter < 10:
        rows.append(y + counter * y)
        counter += 1
    counter = 0
    matrix.append(rows)


for row in matrix:
    row_as_str = list(map(lambda x: str(x), row))
    print(" ".join(row_as_str))
