"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # First pass, sorting the intervals by start time
        # Second pass, comparing from left to right, the end time 
        # to the following interval's start time 


        # Sorting the intervals
        sorted_intervals = sorted(intervals, key=lambda x : x.start)

        # Running a forward comparison pass 
        for i, interval in enumerate(sorted_intervals):
            if i == (len(sorted_intervals) - 1):
                return True

            else:
                if interval.end > sorted_intervals[i+1].start:
                    return False
        return True