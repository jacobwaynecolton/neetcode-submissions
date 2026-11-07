import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # I'm going to be using binary search, so I will create the left and right pointers
        l = 0
        r = max(piles)
        # Starting the max piles value as the current k value (it's the worst case k value)
        last_working_k = max(piles)


        # Creating an eating function for koko
        def koko_eating(h,k):
            for pile in piles:
                if k == 0:
                    return False
                # How long it would take for koko to eat that pile
                time_to_eat = math.ceil(pile/k)
                # Subtract that from our current time 
                h -= time_to_eat
                # If it goes beyond our time return false
                if h < 0 :
                    return False
            return True

        

        while True:
            # If the left and right pointers have crossed, return the current k value
            if l > r:
                break
            # Setting the current k value to the middle between the left and right pointers
            k = (l+r)//2
            
            # Seeing if the current k value works
            if koko_eating(h,k):
                # update the last working k 
                last_working_k = k
                # adjust the pointers to aim for a smaller k value
                r = k-1
            else:
                # adjust the left pointer, as we need a bigger k value
                l = k+1

        return last_working_k

            



        