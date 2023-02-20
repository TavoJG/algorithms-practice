import random
from bubble_sort import bubble_sort, optimized_bubble_sort

from default_sort import default_sort

sample_list = random.sample(range(1, 100), 30)


# Default python sort
print('Default python sort')
sorted_list = default_sort(sample_list)

# Bubble sort
print('Bubble sort - traditional')
bubble_sort_result = bubble_sort(sample_list)
assert sorted_list == bubble_sort_result

# Optimized Bubble sort
print('Bubble sort - optimized')
optimized_bubble_sort_result = optimized_bubble_sort(sample_list)
assert sorted_list == optimized_bubble_sort_result
