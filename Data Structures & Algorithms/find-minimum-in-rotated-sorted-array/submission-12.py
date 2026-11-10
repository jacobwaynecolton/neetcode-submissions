class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initiating pointers at the left and right side of the list
        l, r = 0, len(nums) - 1

        while l < r:
            # Otherwise take the middle between them
            middle = (l + r) // 2
            
            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle 
        return nums[l]