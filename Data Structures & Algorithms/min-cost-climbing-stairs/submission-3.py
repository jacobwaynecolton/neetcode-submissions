class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # Using a dictionary to keep track of the pre-explored climbing
        # sequences
        seen = {}

        # Creating a recursive algorithm to traverse the various climbing
        # sequences
        def climb(cur_step):
            
            # If the top is reached, return 0
            if cur_step > len(cost)-1:
                return 0
            # If the path is already explored, return its value
            if cur_step in seen:
                return seen[cur_step]
            else:
                # Otherwise return the current step value
                # plus the minimum between the two immediate options
                seen[cur_step] = cost[cur_step] + min(climb(cur_step+1), climb(cur_step+2))
                return seen[cur_step]
        # Return the minimum between starting at 0th and 1st index
        return min(climb(0),climb(1))
