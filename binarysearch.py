from typing import List


def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while (left <= right):
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target :
            left = mid + 1
        else: 
            right = mid - 1
    return -1

num = [1,2,3,10]

print(binary_search(num, 3))
print(binary_search(num, 11))