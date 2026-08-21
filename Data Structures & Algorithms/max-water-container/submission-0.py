class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Aim for O(1) space
        
        # Keeping a current max possible area
        max_water = 0

        # Keeping a left and right pointer. One for each extremity of the list
        left = 0
        right = len(heights) - 1

        while left < right: 
            cur_water = (right - left) * min(heights[left],heights[right])
            # Is the current water level better than the max water level previously stored? if so
            # update it
            max_water = max(max_water,cur_water)

            # If the height of the left pointer is less than the right, move it in, otherwise
            # move the right pointer in
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1 
        
        return max_water
            