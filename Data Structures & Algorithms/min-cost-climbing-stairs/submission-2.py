class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        seen = {}

        def climb(cur_step):

            if cur_step > len(cost)-1:
                return 0

            if cur_step in seen:
                return seen[cur_step]
            else:
                seen[cur_step] = cost[cur_step] + min(climb(cur_step+1), climb(cur_step+2))
                return seen[cur_step]

        return min(climb(0),climb(1))
