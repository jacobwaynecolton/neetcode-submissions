import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # My previous solution used division on the input. This of course can lead to many 
        # problems, such as floats not accurately representing large ints (though this 
        # specific problem limits int bit size, so that will not cause issue), or 
        # having to implement roundabout methods to avoid division by zero errors


        # To avoid division, I will keep left and right lists which will store which products
        # will be on either side of a given index i. I can then multiply the respective entries
        # from left and right to get the product of a particular index i in nums

        # Creating the left list 
        left = [1]
        cur_left_prod = 1
        # First including a zero, because the first element of nums has nothing to its left
        # Iterating left to right and stopping 1 short to account for the added 0
        for i in range(len(nums)-1):
            cur_left_prod *= nums[i]
            left.append(cur_left_prod)

        # Creating the right list
        right = [1] * len(nums)
        cur_right_prod = 1
        
        for i in range(len(nums)-2,-1, -1):
            cur_right_prod *= nums[i+1]
            right[i] = cur_right_prod 
        
        # Creating the output list
        output = [num*right[i] for i,num in enumerate(left)]

        return output
         
