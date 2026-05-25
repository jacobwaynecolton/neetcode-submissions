class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):

            # checking if there is a number for total - cur
            if target - num in seen: 
                return [seen[target-num], i]
            seen[num] = i
            