class Solution:
    def rob(self, nums: List[int]) -> int:
        
        max_index = len(nums)

        seen = {}

        if len(nums) == 2:
            return max(nums[0],nums[1])

        def dfs(i):
            if i + 1 >= max_index:
                return nums[i]
            elif i + 2 >= max_index:
                return max(nums[i], nums[i+1])
             
            else:
                if i in seen:
                    return seen[i]
                else:
                    cur = max(nums[i] + dfs(i+2), dfs(i+1))
                    seen[i] = cur
                    return cur

        return dfs(0)