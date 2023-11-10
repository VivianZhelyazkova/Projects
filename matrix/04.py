y = int(input())
my_matrix = []

for element in range(y):
    x = [int(s) for s in input().split()]
    my_matrix.append(x)

diagonal = []

# index = 0
# for x in my_matrix:
#     diagonal.append(x[index])
#     index += 1

for i in range(len(my_matrix)):
    diagonal.append(my_matrix[i][i])

print(diagonal)
