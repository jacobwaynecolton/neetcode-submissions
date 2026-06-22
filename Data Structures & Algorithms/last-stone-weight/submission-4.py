import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        # x is going to be the larger of the two
        x = None
        y = None

        while True:
            print(stones)
            if len(stones) == 1:
                return heapq.heappop_max(stones)
            elif not stones:
                return 0

            if not x:
                x = heapq.heappop_max(stones)

            if not y:
                y = heapq.heappop_max(stones)

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
