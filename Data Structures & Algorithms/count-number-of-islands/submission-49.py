class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Creating a zero array to match the dimensions of grid
        # and keep track of island digits visited
        seen =[[0]*len(grid[0]) for _ in range(len(grid))]
        island_count = 0

        # Creating a depth first search algorithm that will
        # respect the boundaries of the grid and update
        # the seen lists to show which islands have been visited
        def dfs(i,j):
            if seen[i][j] == 1 or grid[i][j] == "0":
                return
            else:
                seen[i][j] = 1
                if j > 0:
                    dfs(i,j-1)
                if i > 0:
                        dfs(i - 1, j)
                if j < len(grid[0])-1:
                    dfs(i,j+1)
                if i < len(grid)-1:
                        dfs(i+1,j)

        # Iterating through each element in the list 
        # if the island hasn't been visited increment island count
        # and dfs from that digit
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    if seen[i][j] == 0:
                        island_count += 1
                        dfs(i,j)
        
        return island_count

                    


