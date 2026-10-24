class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # Keep a set of tuples containing the coordinates of seen tiles

        # Iterate through the entirety of the grid, skip if it lands on a seen tile

        # Use a recursive dfs function to find all vertically and horizontally connected 1's
        # mark those tiles as seen in the process

        seen_coords = set()

        # Keep track of the current highest island size
        max_island_size = 0

        # Creating the recursive searching function
        def dfs(x,y):
            if (x,y) in seen_coords:
                return 0 
            elif grid[x][y] == 0:
                seen_coords.add((x,y))
                return 0
            else:
                seen_coords.add((x,y))
                total = 0
                if x > 0 :
                    top = dfs(x - 1,y)
                    total += top
                if x < len(grid) - 1:
                    bottom = dfs(x + 1,y)
                    total += bottom
                if y < len(grid[0]) - 1:
                    right = dfs(x,y+1)
                    total += right
                if y > 0:
                    left = dfs(x,y-1)
                    total += left
                return 1 + total

        # Iterating through each tile
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in seen_coords:
                    pass
                else:
                    if grid[i][j] == 0:
                        pass
                    else:
                        cur_island_size = dfs(i,j)
                        if cur_island_size > max_island_size:
                            max_island_size = cur_island_size
        
        return max_island_size
