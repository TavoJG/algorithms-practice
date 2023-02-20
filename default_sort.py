from time_count import time_count


@time_count
def default_sort(input: list):
    arr = input.copy()
    arr.sort()
    return arr
