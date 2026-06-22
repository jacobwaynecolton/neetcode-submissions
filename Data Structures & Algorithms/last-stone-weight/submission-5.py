import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Creating a max-heap out of the stones list
        heapq.heapify_max(stones)

        # Keeping track of x and y values though we could go
        # without declaring variables
        x = None
        y = None

        while True:
            # If there is only one stone left, return its weight
            # If there are no stones left, return 0
            if len(stones) == 1:
                return heapq.heappop_max(stones)
            elif not stones:
                return 0

            # If there is no x, or no y, pop from the heap respectively
            if not x:
                x = heapq.heappop_max(stones)
            if not y:
                y = heapq.heappop_max(stones)

            # if they're the same weight, remove both
            # Otherwise remove the smallest and set
            # the largest to it's weight - the smallest's weight
            if x == y:
                x = None
                y = None

            elif x < y:
                y = y - x
                x = None 
                heapq.heappush_max(stones,y)
                y = None
            else:
                x = x - y
                y = None
                heapq.heappush_max(stones,x)
                x = None
