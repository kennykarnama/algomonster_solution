from typing import List

def feasible(weights: List[int], selectedCapacity: int, d: int) -> bool:
    req_days = 1
    i = 0
    n = len(weights)
    capacity = selectedCapacity
    while i < n:
        if weights[i] <= selectedCapacity:
            capacity -= weights[i]
            i = i + 1
        else:
            capacity = selectedCapacity
            req_days = req_days + 1
    return req_days <= d
    
def min_max_weight(weights: List[int], d: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    low = max(weights)
    high = sum(weights)
    boundary_idx = high
    while low <= high:
        mid = (low + high) // 2
        if feasible(weights, mid, d):
            boundary_idx = mid
            high = mid - 1
        else:
            low = mid + 1
    return boundary_idx

if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    d = int(input())
    res = min_max_weight(weights, d)
    print(res)
