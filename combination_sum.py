from typing import Dict, List

def allow(c: List[int], m: Dict[str, bool]):

    x = c.copy()
    x.sort()
    s = str(x)
    #print(s)

    if s in m:
        return False
    
    m[s] = True
    return True

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE

    res = []
    subset_tracker = {}

    def dfs(processed_target: int, paths: List[int], res: List[List[int]], tracker: Dict[str, bool]):
        if processed_target == 0:
            if allow(paths, tracker):
                res.append(paths.copy())
            return
        
        if processed_target < 0:
            return
        
        for c in candidates:
            if processed_target - c < 0:
                continue
            paths.append(c)
            dfs(processed_target - c, paths, res, tracker)
            paths.pop()

        return
    
    dfs(target, [], res, subset_tracker)
    return res

# test mapper

# subsets = [
#     [1,2,3],
#     [3,2,1],
#     [1,1,2,3]
# ]

# m = {}

# for s in subsets:
#     print(allow(s, m))

# print(m)

candidatesOfCandidates = [
    [2,3,5],
    [2,3,6,7],
    [2]
]

targetsOfTargets = [
    8,
    7,
    1
]

for i, c in enumerate(candidatesOfCandidates):
    candidates = c
    target = targetsOfTargets[i]
    print(target, candidates)
    ans = combination_sum(candidates, target)
    print(ans)
