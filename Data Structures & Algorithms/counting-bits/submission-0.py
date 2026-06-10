class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # Creating a final list to store all the binary representations
        final_list = []

        # iterating through each int up to n, and appending 
        # its amount of 1's

        for num in range(n+1):
            count = 0
            for i in range(32):
                if 1 & num:
                    count +=1
                num >>= 1
            final_list.append(count)
        return final_list