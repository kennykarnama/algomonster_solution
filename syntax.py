from collections import Counter, deque
import enum
from typing import List


def printMessage(message):
    print(message)

print("kenny ganteng")

nums = [1,2,3]

# enumerate returns [idx, currentElement]
for idx, val in enumerate(nums):
    print(idx, " -> ", val)

nums.append(5)

# deque
# https://www.geeksforgeeks.org/deque-in-python/

queue = deque(nums)

queue.appendleft

# counter
# https://realpython.com/python-counter/

counter = Counter(set("mississippi"))
print(counter)

popular = counter.most_common(1)
print(popular)

# Tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

r = TreeNode(2)

# loop
def sort_list(unsorted_list: List[int]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(unsorted_list)
    for i in range(0, n-1, 1):
        for j in range (0, n - i - 1, 1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    return unsorted_list

test_data = [3,2,1]
print(sort_list(test_data))
