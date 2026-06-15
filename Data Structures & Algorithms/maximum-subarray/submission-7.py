class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        cur_total = nums[0]
        cur_max = nums[0]

        for i in range(1,len(nums)):
            if cur_total < 0:
                cur_total = nums[i]

            else:
                cur_total += nums[i]
            
            if cur_total > cur_max:
                cur_max = cur_total

        return cur_max

            


            