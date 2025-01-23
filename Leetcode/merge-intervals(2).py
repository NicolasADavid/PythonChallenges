"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

from typing import List
from collections import deque

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        merged = []


        intervals.sort(key = lambda x: x[0])

        intervals = deque(intervals)

        while intervals:
            if not merged:
                merged.append(intervals.popleft())
            else:
                #There is overlap
                if merged[-1][1] >= intervals[0][0]:
                    merged[-1][1] = max(merged[-1][1], intervals[0][1])
                    intervals.popleft()
                else:
                    merged.append(intervals.popleft())

        return merged