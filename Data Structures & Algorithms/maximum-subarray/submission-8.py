class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Keeping track of the current total as we traverse the list
        # of nums left to right
        # Additionally, keeping track of the current maximum
        cur_total = nums[0]
        cur_max = nums[0]

        for i in range(1,len(nums)):
            # If the current total is < 0 replace it with the number
            # at the following index
            # otherwise, add the following number to the current total
            if cur_total < 0:
                cur_total = nums[i]

            else:
                cur_total += nums[i]
            # If the current total is greater than the maximum 
            # update the maximum
            if cur_total > cur_max:
                cur_max = cur_total

        return cur_max

            


            