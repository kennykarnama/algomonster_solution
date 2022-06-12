from typing import List


def insertion_sort(unsorted_list: List[int]) -> List[int]:
    for idx, element in enumerate(unsorted_list):
        current = idx
        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[current]
            current-=1
    return unsorted_list

nums = [3,2,1]

sorted = insertion_sort(nums)

print(sorted)
