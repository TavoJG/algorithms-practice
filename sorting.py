import argparse
from random import sample
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
        pass

    def run(self):
        bubble_sort_result = self.bubble_sort()
        assert self.sorted_list == bubble_sort_result

        optimized_bubble_sort_result = self.optimized_bubble_sort()
        assert self.sorted_list == optimized_bubble_sort_result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run some sort algorithms.')
    sorting = Sorting()
    sorting.run()
