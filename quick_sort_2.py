def quick_sort(arr: list[int]) -> list:
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    left = []
    current = []
    right = []

    for el in arr:
        if el < pivot:
            left.append(el)
        elif el > pivot:
            right.append(el)
        else:
            current.append(el)

    return quick_sort(left) + current + quick_sort(right)


print(quick_sort([1, 4, 2, 56, 3, 3, 7, 34, 7, 3, 55, 90]))
