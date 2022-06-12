from typing import List

def find_first_occurrence(arr: List[int], target: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr) - 1
    solution_idx = -1
    while(left <= right):
        mid = (left + right) // 2
        if arr[mid] >= target:
            if target == arr[mid]:
                solution_idx = mid
            right = mid - 1
        else:
            left = mid + 1
    return solution_idx

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = find_first_occurrence(arr, target)
    print(res)