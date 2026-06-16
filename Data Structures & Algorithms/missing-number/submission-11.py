class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Keeping track of the total bits
       total = len(nums)
        # Iterating through each num in nums
        # xor is used to cancel out each num with the indices
        # if a num is missing, the index will remain. Or
        # if it's missing the total length (n) that will be returned
       for i,num in enumerate(nums):
            total ^= num ^ i

  
       return total