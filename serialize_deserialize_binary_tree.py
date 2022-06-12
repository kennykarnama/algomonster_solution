from copyreg import constructor


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    # WRITE YOUR BRILLIANT CODE HERE
    nodes = []
    
    def dfs(root: Node):
        if root == None:
            nodes.append('NULL')
            return
        nodes.append(str(root.val))
        dfs(root.left)
        dfs(root.right)
    
    dfs(root)
  
    return ",".join(nodes)

def deserialize(serialized_nodes):
    s = []
    serialized_nodes.split(",")
    r = Node(serialized_nodes[0])
    
    idx = 0
    def construct(n: Node, level: int):
        if idx + 1 < len(serialized_nodes) and serialized_nodes[idx+1] != 'NULL':
            n.left = Node(serialized_nodes[idx+1])
            idx += 1
            construct(n.left, level + 1)
        elif idx + 2 < len(serialized_nodes) and serialized_nodes[idx+2] != 'NULL':
            n.right = Node(serialized_nodes[idx+2])
            idx += 2
            construct(n.right, level + 1)
        elif level == 0:
            if n.right == None:
                construct(n.right, level + 1)
    
    construct(r, 0)

    return r

r = Node(5)
r.left = Node(4)

n1 = Node(7)
n1.left = Node(6)
n1.right = Node(9)

r.right = n1

serialized = serialize(r)
# print(serialized)

deserialized = deserialize(serialized)
print(deserialized)
