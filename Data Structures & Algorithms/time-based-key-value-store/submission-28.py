class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If that key is already in the map dict
        if key not in self.map:
            self.map[key] = [(timestamp,value)]
        else:
            # Otherwise, add it to the map dict
            self.map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        # Performing binary search on the list of tuples to get the desired timestamp
        # if not, the most recently prior,
        # if there are none prior return ""
        if key not in self.map:
            return ""
        tuples = self.map[key]
        
        l,r = 0, len(tuples) - 1
        highest_lessthan_timestamp_val = None
        while l <= r:

            # middle index
            middle = (l+r) // 2

            # If the element is at the middle index return
            if tuples[middle][0] == timestamp:
                return tuples[middle][1]
            
            # Otherwise check if the value at that middle index is < or > the desired timestamp
            if tuples[middle][0] > timestamp:
                r = middle - 1
            else:
                l = middle + 1
                highest_lessthan_timestamp_val = tuples[middle][1]

        if highest_lessthan_timestamp_val:
            return highest_lessthan_timestamp_val
        else:
            return ""
                
       

