my_list = input().split()
symbol = input()


def list_of_indexes(some_list, char):
    list_of_index = [some_list.index(x) for x in some_list if char in x]
    return list_of_index


if list_of_indexes(my_list, symbol):
    print(list_of_indexes(my_list, symbol))
else:
    print("Not found!")
