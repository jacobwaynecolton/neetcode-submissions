class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       bits = len(nums)

       for i,num in enumerate(nums):
            bits ^= num ^ i

  
       return bits