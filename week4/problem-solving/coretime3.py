str_grid = [["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]]

grid = [list(map(int, row)) for row in str_grid]
visited = [[False] * len(grid[0]) for _ in range(len(grid))]

print(grid)
print(visited)
