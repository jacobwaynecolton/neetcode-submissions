class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initiating pointers at the left and right side of the list
        l, r = 0, len(nums) - 1

        # If l < r, l is the minimum, no rotations occurred
        if nums[l] < nums[r]:
            return nums[l]

        while True:
            # Otherwise take the middle between them
            middle = (l + r) // 2
            
            # If the value to the left of the middle is
            # > it, we found the min
            if l == r:
                return nums[l]
            
            if nums[middle-1] > nums[middle]:
                return nums[middle]


            # If the middle is > l, the min is on the right side of the list
            # move the l pointer accordingly
            if nums[middle] >= nums[l]:
                l = middle + 1
                if nums[l-1] > nums[l]:
                    return nums[l]
            else:
                r = middle - 1