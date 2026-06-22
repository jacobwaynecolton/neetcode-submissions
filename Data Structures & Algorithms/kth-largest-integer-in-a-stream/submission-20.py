import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Sorting the incoming list from largest to smallest,
        # then, only keeping the k-largest elements
        sorted_list = sorted(nums,reverse=True)[:k]
        self.k = k
        # Converting it into a min-heap so it will be easy enough
        # to get the current k largest
        heapq.heapify(sorted_list)
        self.nums = sorted_list

    def add(self, val: int) -> int:
        # Adding the new element 
        heapq.heappush(self.nums,val)
        # checking if this makes the heap larger than it should be
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # return the current k largest
        return self.nums[0]