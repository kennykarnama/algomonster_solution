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

def count_number_of_islands(grid: List[List[int]]) -> int:

    num_rows, num_cols = len(grid), len(grid[0])

    def bfs(root, grid):
        
        q = deque([root])
        
        while len(q) > 0:
            current_node = q.popleft()

            c_r, c_y = current_node
            
            if grid[c_r][c_y] == 0:
                continue
            
            neighbors = get_neighbors(current_node, num_rows, num_cols)
            for neighbor in neighbors:
                x, y = neighbor
                if grid[x][y] == 1:
                    q.append(neighbor)
            
            grid[c_r][c_y] = 0
            
        return

    islands = 0

    for r in range (num_rows):
        for c in range(num_cols):
            if grid[r][c] == 1:
                islands += 1
                bfs((r,c), grid) 
    
    return islands

grid = [
    [1,1,1,0,0,0],
    [1,1,1,1,0,0],
    [1,1,1,0,0,0],
    [0,1,1,1,1,0],
    [0,0,0,0,1,0],
    [0,0,0,0,0,0]
]

islands = count_number_of_islands(grid)

print(islands)