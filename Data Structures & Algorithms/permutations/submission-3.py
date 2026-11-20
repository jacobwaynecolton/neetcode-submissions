class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Return the output array
        out = []
        # Update the current array
        current = []

        # Keeping track of the already chosen #'s with a hashmap
        already_picked = set() 

        def dfs(cur_i):
            if cur_i == len(nums) :
                out.append(current.copy())
                return
            
            for i in range(0,len(nums)):
                if nums[i] in already_picked:
                    continue
                
                current.append(nums[i])
                already_picked.add(nums[i])
                dfs(cur_i+1)
                current.pop()
                already_picked.remove(nums[i])

        dfs(0)
        return out