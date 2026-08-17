import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # So, if there is more than one zero, that means that even if we exclude a zero at 
        # index i, the product will still be zero. However, this of course does not apply if
        # index i has the only zero in the list. Therefore, there will be a special rule for 
        # a single zero and >1

        zero_count = 0
        total_prod = 1
        output = []

        for num in nums:
            if num == 0:
                zero_count +=1
            else:
                total_prod *= num

        for num in nums:
            if zero_count == 0:
                # converting the appended element to an integer because division converts it to a
                # float, and the output elements must be integers
                output.append(int(total_prod/num))
            elif zero_count == 1 and num == 0:
              
                output.append(total_prod)
            else:
                output.append(0)


        return output
