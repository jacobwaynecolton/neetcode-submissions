class Solution:
    def climbStairs(self, n: int) -> int:
        # Including a list of all the seen steps
        # for example, if we have already been to step 25/40
        # we know the remaining path combinations from that point on
        seen = {}

        # Creating a recursive function to traverse all paths to n
        def climb(jump_size,n,cur_pos):

            new_pos = cur_pos + jump_size
            # If this combination/path reaches n
            if new_pos == n:
                return 1
            # If this combination is invalid
            elif new_pos > n:
                return 0 
            # Add this position to seen if it has never been seen before
            if new_pos in seen:
                return seen[new_pos]
            else:
                seen[new_pos] = climb(1,n,new_pos) + climb(2,n,new_pos)
                return seen[new_pos]

        total = climb(1,n,0) + climb(2,n,0)

        return total
