class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        final_index = len(nums) - 1

        def dfs(index):

            
            # Base case 
            if index == final_index:
                return True
            elif index > final_index:
                return False
            elif nums[index] == 0:
                return False

            else:
                nums[index] -= 1
                return dfs(index + nums[index] + 1) or dfs(index)
                
        return dfs(0)


    