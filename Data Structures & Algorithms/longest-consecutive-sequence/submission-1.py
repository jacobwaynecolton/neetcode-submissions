class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Reanswer this but use a set
        # - removes duplication
        # - uses hash table like a dictionary for O(1) lookup


        # O(n) to convert the list to a set, and it of course
        # does not order the items

        nums_set = set(nums)
        longest_sequence = 0

        # Iterating through each number in the set
        for num in nums_set:
            current_sequence = 1
            # Checking if the set contains a number lower than it
            # if not, progress through that sequence
            if (num - 1) not in nums_set:
                counter = num
                while (counter + 1) in nums_set:
                    counter += 1
                    current_sequence +=1
                
                longest_sequence = max(current_sequence,longest_sequence)
        return longest_sequence
