from collections import deque


def get_neighbors(coord, num_rows, num_num_cols):
    row, col = coord
    
    delta_row = [-2, -2, -1, 1, 2, 2, 1, -1]
    
    delta_col = [-1, 1, 2, 2, 1, -1, -2, -2]

    res = []

    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]

        if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_num_cols:
            res.append((neighbor_row, neighbor_col))
    
    return res

def get_knight_shortest_path(x: int, y: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    num_rows = 7
    num_cols = 7

    destination = (x,y)

    # first and second is coordinate
    # third is steps
    root = (0,0,0)

    def bfs(root) -> int:
        
        q = deque([root])

        visited = [[False for c in range(num_cols)] for r in range(num_rows)]
        
        while len(q) > 0:

            current_node = q.popleft()

            c_r, c_y, steps = current_node
            
            if visited[c_r][c_y] == True:
                continue

            if (c_r, c_y) == destination:
                return steps
            
            neighbors = get_neighbors((c_r, c_y), num_rows, num_cols)
            #print(neighbors)
            for neighbor in neighbors:
                n_x, n_y = neighbor
                q.append((n_x, n_y, steps+1))
            
            visited[c_r][c_y] = True
            
        return 0
    
    minimum_path = bfs(root)

    return minimum_path

test_cases = [
    (1,2),
    (5,5)
]

for test_case in test_cases:
    x, y = test_case
    print(get_knight_shortest_path(x,y))