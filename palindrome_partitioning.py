from importlib.resources import path
from typing import List

# check if string is palindrome
def palindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1

    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    
    return True
def partition(s: str) -> List[List[str]]:
    # WRITE YOUR BRILLIANT CODE HERE

    res = []
    def dfs(start_idx: int, res: List[List[str]], paths: List[str]):
        if start_idx == len(s):
            res.append(paths.copy())
            return
        
        if start_idx > len(s):
            return
        
        for i in range (len(s)):
            candidate = s[start_idx:(start_idx + i + 1)]
            if palindrome(candidate):
                paths.append(candidate)
                dfs(start_idx + i + 1, res, paths)
                paths.pop()

        return
    
    dfs(0, res, [])
    return res

# test palindrome

# words = [
#     "a",
#     "aa",
#     "ab",
#     "aba"
# ]

# for w in words:
#     print(palindrome(w))

t = "aab"

print(partition(t))