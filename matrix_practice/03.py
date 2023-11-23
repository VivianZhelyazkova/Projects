y = int(input())
my_matrix = []

for element in range(y):
    x = [int(s) for s in input().split()]
    my_matrix.append(x)

max_sum = 0
for index, x in enumerate(my_matrix):
    if sum(x) > max_sum:
        max_sum = sum(x)
        max_index = index

print(max_index)