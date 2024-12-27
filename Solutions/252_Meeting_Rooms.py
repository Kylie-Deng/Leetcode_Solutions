from typing import List


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) <= 1:
            return True

        intervals.sort(key=lambda x: x.start)
        endTime = intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start < endTime:
                return False
            endTime = intervals[i].end

        return True