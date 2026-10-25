from collections import deque

class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Implement BFS. --First I tried DFS, but I realized that BFS can make use of a 'seen' matrix because the path which
        # contacts a node first is guaranteed to be the best path to it (from that particular 0). This was not the case
        # with DFS, so I couldn't mark off nodes.


        def bfs(i,j,counter):

            # Using a queue and a while loop
            # Wrap in a list so the tuple goes in as one element
            queue = deque([(i,j,counter)])
            seen = set()
            

            while queue:

                # Pop from the front so closer cells get processed first
                cur_node = queue.popleft()
                i = cur_node[0]
                j = cur_node[1]
                c = cur_node[2]

                # Skip if already visited this run or if it's a wall
                if (cur_node[0],cur_node[1]) in seen or grid[i][j] == -1:
                    continue
                # Mark as seen
                seen.add((i,j))
                # Found a shorter distance than what's stored, update it
                if grid[i][j] > c:
                    grid[i][j] = c
                # Another treasure already got here at least as close, so no point spreading from here
                # (c > 0 so the starting treasure doesn't prune itself)
                elif c > 0 and grid[i][j] > -1 and grid[i][j] <= c:
                    continue
                # Add in-bounds neighbors one step further out
                if i > 0:
                    queue.append((i-1,j,c+1))
                if j > 0:
                    queue.append((i,j-1,c+1))
                if i < len(grid) - 1:
                    queue.append((i+1,j,c+1))
                if j < len(grid[0]) - 1:
                    queue.append((i,j+1,c+1))
                

                    
        # Run a BFS from every treasure, keeping the min distance in grid
        for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 0:
                        bfs(i,j,0)