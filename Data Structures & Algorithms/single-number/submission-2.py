class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        

        # Converting each num in nums to bits,
        # then using the bits as indices

        # Creating a frequency dict
        num_freq = {}

        for num in nums :
            bin_key = bin(num)
            num_freq[bin_key] = num_freq.get(bin_key,0) + 1
        
        for freq in num_freq:
            if num_freq[freq] == 1:
                return int(freq,2)
