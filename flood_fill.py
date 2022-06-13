from collections import deque
from typing import List


def get_neighbors(coord, num_rows, num_num_cols):
    row, col = coord
    
    delta_row = [-1, 0, 1, 0]
    
    delta_col = [0, 1, 0, -1]

    res = []

    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]

        if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_num_cols:
            res.append((neighbor_row, neighbor_col))
    
    return res

def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    num_rows, num_cols = len(image), len(image[0])

    q = deque([(r,c)])

    target_val = image[r][c]

    visited = [[False for c in range(num_cols)] for r in range(num_rows)]

    while len(q) > 0:

        row, col = q.popleft()

        if visited[row][col]:
            continue

        if image[row][col] == target_val:
            image[row][col] = replacement

        neighbors = get_neighbors((row, col), num_rows, num_cols)

        for neighbor in neighbors:
            x, y = neighbor
            q.append(neighbor)
        
        visited[row][col] = True

    return image

r = 2
c = 2
replacement = 9
arr = [[0,1,3,4,1],[3,8,8,3,3],[6,7,8,8,3],[12,2,8,9,1],[12,3,1,3,2]]

ans = flood_fill(r,c,replacement,arr)

print(ans)