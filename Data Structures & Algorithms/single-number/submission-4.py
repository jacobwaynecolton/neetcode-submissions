class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        

        # Using XOR on the bits so all the 
        # nums with two instances will cancel each other out
        # leaving only the num with a single instance

        final_num = 0

        for num in nums : 
            final_num ^= num

        return final_num

