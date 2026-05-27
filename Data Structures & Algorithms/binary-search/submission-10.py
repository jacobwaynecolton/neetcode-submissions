class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search
        # Get the index for the middle of the array
        mid_index = len(nums) // 2

        # If the target resides in the middle, return its index
        if target == nums[mid_index]:
            return mid_index
        
        # If the list only contains one item
        elif len(nums) == 1:
            return -1

        # If the target is less than our current middle value
        # recursive call on first half of list
        if target < nums[mid_index]:
            recursive_val = self.search(nums[:mid_index], target)
            # if the returned value is -1 simply return that 
            if recursive_val < 0:
                return -1 
            else:
                return recursive_val
        else:
            recursive_val = self.search(nums[mid_index:], target)
            # if the returned value is -1 simply return that 
            if recursive_val < 0:
                return -1 
            else:
                return mid_index + recursive_val