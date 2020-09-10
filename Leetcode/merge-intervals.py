from typing import List

class Solution:

    # interval: [start,end]
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # sort the intervals by start (1st element)
        intervals = sorted(intervals, key=lambda x: x[0])

        # begin with interval with the lowest start value 
        out = [intervals.pop(0)]

        while intervals:
            # get next interval
            start, end = intervals.pop(0)

            # if start overlaps with the last interval of out
            if start > out[-1][1]:
                # add new distinct interval
                out.append((start, end))
            else:
                # replace last interval with a merged interval
                out[-1] = (out[-1][0], max(out[-1][-1], end))

        return out         

if __name__ == "__main__":

    s = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]

    r = s.merge(intervals)

    print(r)


