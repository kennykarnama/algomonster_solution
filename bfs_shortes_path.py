from typing import List


def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    
    q = []

    q.append([a])

    level = 0

    visited = {}

    while len(q) > 0:
        
        nodes = q.pop()
        
        p = []
        
        for n in nodes:

            # print(n)
            
            if n in visited:
                continue

            if n == b:
                return level

            if b in graph[n]:
                return level + 1
            
            p += graph[n]
            
            visited[n] = True
        
        if len(p) > 0:
            q.append(p.copy())
        
        level += 1

    return level

# graph = [

#     [1,2],
#     [0,2,3],
#     [0,1],
#     [1]
# ]

graph = [
    [1,2],
    [0,2,3],
    [0,1,6],
    [1, 4],
    [3, 5],
    [4, 6],
    [2, 5]
]

a = 5
b = 0

ans = shortest_path(graph, a, b)

print(ans)