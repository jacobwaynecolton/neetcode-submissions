class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # First, I will sort the list of nums 
        # Sorted() creates a new list, .sort() sorts in place. I will use sorted()
        nums_sort = sorted(nums)

        # Keeping track of which number combinations = 0
        num_comb = []

        # Now, with this sorted list, I will iterate through each num, for each iteration, I will also
        # have two pointers closing in on each other, one being a max pointer and one being a min pointer.
        # the min pointer will begin just after the current index i
        # Duplicate number entries will also be skipped

        for i, num in enumerate(nums_sort):
            max = len(nums_sort)-1
            min = i + 1

            # If you are on an entry i with duplicates, skip to the final duplicate
            if i > 0 and num == nums_sort[i-1]:
                continue
            while min < max: 
                sum = nums_sort[max] + nums_sort[min] + num
                # If the current sum in 0
                if sum == 0: 
                    num_comb.append([num,nums_sort[min],nums_sort[max]])
                    # Now, we need to account for the fact that the min or max may be on a duplicate #
                    while min < (len(nums) - 1) and nums_sort[min] == nums_sort[min + 1]:
                        min +=1
                    while max > 1 and nums_sort[max] == nums_sort[max -1]:
                        max -=1
                    min +=1
                    max -=1
                elif sum > 0: 
                    max -= 1
                else :
                    min += 1
        return num_comb


