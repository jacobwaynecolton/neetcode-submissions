class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Using the mathematical approach
        total = 0
        for digit in digits: 
            total = (total * 10) + digit
        total += 1

        return [int(x) for x in str(total)]