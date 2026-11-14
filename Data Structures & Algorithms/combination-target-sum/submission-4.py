class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
       
        outputs = [] 

        def backtrack(cur_list,total,index):
            # Next time i should sort first, that way i can
            # prune the later iterations of the for loop off

            # Base cases
            if total == target:
                outputs.append(cur_list)
                return
            if total > target:
                return

            for i in range(index,len(nums)):
                backtrack(cur_list + [nums[i]],total + nums[i],i)



        backtrack([],0,0)
            
        return outputs
            
