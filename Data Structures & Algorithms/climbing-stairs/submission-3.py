class Solution:
    def climbStairs(self, n: int) -> int:
        
        seen = {}

        def climb(jump_size,n,cur_pos):

            new_pos = cur_pos + jump_size

            if new_pos == n:
                return 1
            elif new_pos > n:
                return 0 

            if new_pos in seen:
                return seen[new_pos]
            else:
                seen[new_pos] = climb(1,n,new_pos) + climb(2,n,new_pos)
                return seen[new_pos]

        total = climb(1,n,0) + climb(2,n,0)

        return total
