from time_count import time_count


@time_count
def bubble_sort(input: list):
    arr = input.copy()

    n = len(arr)

    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


@time_count
def optimized_bubble_sort(input: list):
    arr = input.copy()

    n = len(arr)

    exchange_exists = False

    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                exchange_exists = True

            if not exchange_exists:
                break

    return arr
