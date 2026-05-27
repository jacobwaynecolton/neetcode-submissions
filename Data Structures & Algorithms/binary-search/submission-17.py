class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search
        # Now writing it as a loop instead of a recursive function
        # This is because i dont want to mess around with the function
        # definition and it currently lacks the index parameters

        left = 0
        right = len(nums) - 1

        while left <= right: 
            # Get the center index
            mid_index = (left + right) // 2
            print(nums[mid_index])
            # Check if the target lies at the middle index
            if target == nums[mid_index]:
                # Return that index if so
                return mid_index
            
            # If the mid_index lies further ahead than the target
            if target < nums[mid_index]:
                right = mid_index - 1
            
            # Otherwise / if the target is larger than the middle of the list
            else:
                left = mid_index + 1
        

        # Target not found
        return -1