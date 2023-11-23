number = int(input())
matrix = []

for y in range(number):
    rows = []
    for x in range(number):
        if y % 2 == 0:
            rows.append("# ")
        else:
            rows.append(" #")
    matrix.append(rows)

for row in matrix:
    print("".join(row))