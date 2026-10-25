from collections import deque

class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Implement BFS. --First I tried DFS, but I realized that BFS can make use of a 'seen' matrix because the path which
        # contacts a node first is guaranteed to be the best path to it (from that particular 0). This was not the case
        # with DFS, so I couldn't mark off nodes.


        def bfs(i,j,counter):

            # Using a queue and a while loop
            queue = deque([(i,j,counter)])
            seen = set()
            

            while queue:

                cur_node = queue.popleft()
                i = cur_node[0]
                j = cur_node[1]
                c = cur_node[2]

                if (cur_node[0],cur_node[1]) in seen or grid[i][j] == -1:
                    continue
                # Mark as seen
                seen.add((i,j))
                if grid[i][j] > c:
                    grid[i][j] = c
                elif c > 0 and grid[i][j] > -1 and grid[i][j] <= c:
                    continue
                if i > 0:
                    queue.append((i-1,j,c+1))
                if j > 0:
                    queue.append((i,j-1,c+1))
                if i < len(grid) - 1:
                    queue.append((i+1,j,c+1))
                if j < len(grid[0]) - 1:
                    queue.append((i,j+1,c+1))
                

                    
        for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 0:
                        bfs(i,j,0)    
        
