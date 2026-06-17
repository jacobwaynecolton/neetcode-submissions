class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bits = 0

        # Looping over all 32 bits
        for i in range(32):
            cur_bit = 1 & n

            # push one bit off the right side of n
            n >>= 1

            # push reversed bits to the left one to make room
            # for the new bit 
            reversed_bits <<= 1

            # bring the new bit in from right to left
            reversed_bits |= cur_bit

        
        return reversed_bits