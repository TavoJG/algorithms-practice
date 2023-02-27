import argparse
from random import sample, randint
from time_count import time_count


class Sorting:

    def __init__(self, sample_size=20, sample_range=100) -> None:
        self.sample_list = sample(range(1, sample_range), sample_size)
        self.sorted_list = self.default_sort()

    def _copy_sample(self) -> list:
        return self.sample_list.copy()

    @time_count
    def default_sort(self):
        arr = self._copy_sample()
        arr.sort()
        return arr

    @time_count
    def bubble_sort(self):
        arr = self._copy_sample()
        n = len(arr)

        for i in range(n):
            for j in range(n-1-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr

    @time_count
    def optimized_bubble_sort(self):
        arr = self._copy_sample()
        n = len(arr)
        exchange_exists = False

        for i in range(n):
            for j in range(n-1-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    exchange_exists = True

                if not exchange_exists:
                    break

        return arr

    @time_count
    def inserting_sort(self):
        arr = self._copy_sample()
        n = len(arr)

        for i in range(1, n):
            j = i - 1

            while j >= 0 and arr[j] > arr[i]:
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = arr[i]

        return arr

    def _merge_sorted_arrays(self, left: list, right: list) -> list:
        if len(left) == 0:
            return right

        if len(right) == 0:
            return left

        result = []

        index_left = index_right = 0

        while len(result) < len(left) - len(right):
            if left[index_left] <= right[index_right]:
                result.append(left[index_left])
                index_left += 1
            else:
                result.append(right[index_right])
                index_right += 1

            if index_right == len(right):
                result += left[index_left:]
                break

            if index_left == len(left):
                result += right[index_right:]
                break

        return result

    def _sort_merge(self, input: list) -> list:
        if len(input) < 2:
            return input

        midpoint = len(input) // 2

        return self._merge_sorted_arrays(left=self._sort_merge(input[:midpoint]), right=self._sort_merge(input[midpoint:]))

    @time_count
    def merge_sort(self):
        arr = self._copy_sample()
        result = self._sort_merge(arr)
        return result

    def _quick_sort(self, input: list) -> list:
        if len(input) < 2:
            return input

        pivot = input[randint(0, len(input)-1)]

        low, equal, high = [], [], []

        for el in input:
            if el < pivot:
                low.append(el)
            elif el == pivot:
                equal.append(el)
            else:
                high.append(el)

        return self._quick_sort(low) + equal + self._quick_sort(high)

    @time_count
    def quick_sort(self):
        arr = self._copy_sample()
        result = self._quick_sort(arr)
        return result

    def run(self):
        bubble_sort_result = self.bubble_sort()
        assert self.sorted_list == bubble_sort_result

        optimized_bubble_sort_result = self.optimized_bubble_sort()
        assert self.sorted_list == optimized_bubble_sort_result

        inserting_sort_result = self.inserting_sort()
        assert self.sorted_list == inserting_sort_result

        sort_merge_result = self.merge_sort()
        assert self.sorted_list == sort_merge_result

        quick_sort_result = self.quick_sort()
        assert self.sorted_list == quick_sort_result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run some sort algorithms.')
    sorting = Sorting()
    sorting.run()
