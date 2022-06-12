from typing import List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    q = []
    q.append([root])
    res = []
    while len(q) > 0:
        nodes = q.pop()
        p = []
        level_res = []
        for n in nodes:
            if n.left != None:
                p.append(n.left)
            if n.right != None:
                p.append(n.right)
            level_res.append(n.val)
        
        if len(level_res) > 0:
            res.append(level_res.copy())
        
        if len(p) > 0:
            q.append(p.copy())

    return res

r = Node(1)
c1 = Node(2)
c2 = Node(3)
c2_2 = Node(6)
c_11 = Node(4)
c_12 = Node(5)
c_11_2 = Node(7)

r.left = c1
r.right = c2
c1.left = c_11
c1.right = c_12
c2.right = c2_2

c_11.right = c_11_2

ans = level_order_traversal(r)

print(ans)
