matrix = [
        [1, 2, 3, 4],
        [7, 4, 5, 6],
        [7, 7, 8, 9],
        [8, 7, 6, 5]
    ]


def most_common_with_flatten_list_with_comprehension(lst):
    flatlist = [el for sublist in lst for el in sublist]
    most_frequent_element = max(flatlist, key=flatlist.count)
    how_many_times_we_say_it = flatlist.count(most_frequent_element)
    print(f'Most frequent element is {most_frequent_element} and we see it {how_many_times_we_say_it} times.')


most_common_with_flatten_list_with_comprehension(matrix)
