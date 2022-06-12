from tracemalloc import start
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    def dfs(start_idx: int, paths: List[int], res: List[List[int]], desired: int):
        if len(paths) == desired:
            res.append(paths.copy())
            return
        
        if start_idx == len(nums):
            return
        
        i = start_idx

        while i < len(nums):
            paths.append(nums[i])
            dfs(i+1, paths, res, desired)
            paths.pop()
            i += 1
        
        return
    
    res = []

    for desired in range (len(nums) + 1):
        dfs(0, [], res, desired)

    return res

nums = [1,2,3]

ans = subsets(nums)

print(ans)