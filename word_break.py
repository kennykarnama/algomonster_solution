from tracemalloc import start
from typing import List


def word_break(s: str, words: List[str]) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    def dfs(start_idx: int):
        if start_idx == len(s):
            return True
        
        for word in words:
            if s[start_idx:].startswith(word):
                if dfs(start_idx + len(word)):
                    return True
        
        return False
    return dfs(0)

def word_break_memo(s: str, words: List[str]) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    memo = {}
    def dfs(start_idx: int):
        if start_idx == len(s):
            return True
        
        if start_idx in memo:
            return memo[start_idx]
        
        ok = False
        for word in words:
            if s[start_idx:].startswith(word):
                if dfs(start_idx + len(word)):
                    ok = True
                    break
        
        memo[start_idx] = ok
        
        return ok

    return dfs(0)

print(word_break_memo("aab", ["a", "aa", "b"]))

