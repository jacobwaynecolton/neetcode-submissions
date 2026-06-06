class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using a dictionary to store the counts for each number 
        # Using bucket sort to solve this problem
        # Creating the buckets
        buckets = [[] for x in range(len(nums) + 1)]
        # Creating the dictionary to keep track of the counts for each
        # number in nums
        freq_nums = {}
        for num in nums:
            # If the number doesn't already exist in nums, create it 
            # at zero. Otherwise, increment
            freq_nums[num] = freq_nums.get(num, 0) + 1
        
        # Now, iterating through the created dictionary,
        # inputting each element into their respective buckets
        for freq in freq_nums:
            buckets[freq_nums[freq]].append(freq)
        # Creating the final list to return and tracking current k
        k_nums = []
        counter = k
        
        # Iterating backwards through the buckets, to give the k largest
        for bucket in reversed(buckets):
            if counter == 0:
                break
            else:
                if len(bucket) == 0:
                    pass
                else:
                    k_nums.extend(bucket)
                    counter -= len(bucket)
        return k_nums