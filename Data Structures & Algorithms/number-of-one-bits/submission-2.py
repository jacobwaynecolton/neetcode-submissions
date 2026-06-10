class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0


        for i in range(32): 
            # Checking if the final number is a 1
            # If so, increment the counter
            if n & 1:
                counter +=1
            # Shift n to the right by one
            n >>= 1 
        return counter