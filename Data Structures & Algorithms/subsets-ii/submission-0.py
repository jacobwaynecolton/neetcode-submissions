class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # output list
        out = []

        # current list
        cur = []

        # sort the list
        nums = sorted(nums)

        def dfs(idx):
            if(idx == len(nums)):
                out.append(cur.copy())
                return

            cur.append(nums[idx])
            dfs(idx+1)
            cur.pop()

            while idx < len(nums) - 1 and nums[idx+1] == nums[idx]:
                idx += 1
            
            dfs(idx + 1)
            




        dfs(0)

        return out
