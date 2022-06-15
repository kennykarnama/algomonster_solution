import copy
from typing import List

INF = 2147483647

def map_gate_distances(dungeon_map: List[List[int]]) -> List[List[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    num_rows, num_cols = len(dungeon_map), len(dungeon_map[0])

    delta_row = [-1, 0, 1, 0]
    
    delta_col = [0, 1, 0, -1]

    result = copy.deepcopy(dungeon_map)

    def dfs(g: List[List[int]], o_x: int, o_y: int, visited: set) -> int:
        
        if o_x < 0 or o_x >= num_rows:
            return INF

        if o_y < 0 or o_y >= num_cols:
            return INF
        
        if g[o_x][o_y] == 0:
            return 0

        if g[o_x][o_y] != INF:
            return INF

        
        minima = INF

        visited.add((o_x, o_y))

        for pos in range (len(delta_row)):
            d_x = o_x + delta_row[pos]
            d_y = o_y + delta_col[pos]

            if (d_x, d_y) in visited:
                continue

            # visited.add((d_x, d_y))

            distance = 1 + dfs(g, d_x, d_y, visited)

            if distance < minima:
                minima = distance
        
        return minima

    for r in range (num_rows):
        for c in range (num_rows):
            if dungeon_map[r][c] == INF:
                # print(r,c)
                visited = set()
                minima = dfs(dungeon_map, r, c, visited)
                result[r][c] = minima

    return result

# test

dungeon_map = [
  [INF, -1, 0, INF],
  [INF, INF, INF, -1],
  [INF, -1, INF, -1],
  [0, -1, INF, INF],
]

ans = map_gate_distances(dungeon_map)

print(ans)