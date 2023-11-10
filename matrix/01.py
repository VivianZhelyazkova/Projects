numbers = [int(x) for x in input().split()]


def is_positive(some_list):
    positive_numbers = list(filter(lambda s: s > 0, some_list))
    return len(positive_numbers) == len(some_list)


print(is_positive(numbers))
