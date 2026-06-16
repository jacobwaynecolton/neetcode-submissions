class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Using a more efficient mathematical approach
        # where carry-over is used

        # Iterating backwards through the list of digits
        # With range, it is non inclusive with the ending number
        for i in range(len(digits) - 1, -1,-1):
            # If the number is < 9 you can simply increment it by 1
            # Once the incrementing has occured, the list 
            # can be returned as it is
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # otherwise set the digit to 0
            # and move on to the next digit 
            else:
                digits[i] = 0
            
        # Concatenating a 1 on to the front of the list
        # If the list reaches the end without incrementing 
        # the total sum
        return [1] + digits