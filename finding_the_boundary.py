from typing import List

def find_boundary(arr: List[bool]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, len(arr) - 1
    while (left <= right):
        mid = (left + right) // 2
        if arr[mid] == False:
            left = mid + 1
        else:
            if mid - 1 >= 0:
                if arr[mid-1] == True:
                    right = mid - 1
                else:
                    return mid
            else:
                return mid
    return -1

if __name__ == '__main__':
    arr = [x == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)
