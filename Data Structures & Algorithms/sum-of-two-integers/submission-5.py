class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # summation using 2's complement for the negative numbers
        # will be the same process for addition and subtraction

        # Creating a loop, utilizing XOR to isolate the bits
        # which don't require carry-over, and 'AND' for the bits
        # which require carry over

        # shifting the carry bits to the left by one, then
        # restarting the loop. Summing the XOR and AND bits


        while True: 
            # Python has arbitrary precision, so let's mask 
            # to 32 bits to immitate fixed precision
            a &= 0xFFFFFFFF
            b &= 0xFFFFFFFF

            if b == 0:
                # undoing the mask if the signed bit indicates
                # the number is negative
                if a & 0x80000000 != 0: 
                    return a - (2 ** 32)

                return a

            XOR_bits = a ^ b
            carry_bits = a & b

            carry_bits <<= 1

            a = XOR_bits
            b = carry_bits

