from typing import List
from collections import defaultdict

# class Solution:

#     def calcArea(self, bl, br, tl, tr) -> int:
        
#         xdiff = br[0] - bl[0]
#         ydiff = tl[1] - br[1]

#         return abs(xdiff * ydiff)

#     """
#     Takes too long
#     """
#     def minAreaRectSlow(self, points: List[List[int]]) -> int:

#         # collect points with same y value ( pair of points has to be parallel to x meaning y value is the same) (straight line)
#         # collect points with same x value

#         pointTuples = []


#         pointXMap = defaultdict(set) # Collect points by their x value
#         pointYMap = defaultdict(set) # Collect points by their y value

#         bestArea = None

#         for x, y in points:
#             pointXMap[x].add((x, y))
#             pointYMap[y].add((x, y))
#             pointTuples.append((x, y))

#         for p1 in pointTuples:

#             x1, y1 = p1
            
#             pointsUsed = set()
#             pointsUsed.add(p1)

#             for matchingP1YPoint in pointYMap[y1]:

#                 if matchingP1YPoint in pointsUsed:
#                     continue
#                 pointsUsed.add(matchingP1YPoint)

#                 x2, y2 = matchingP1YPoint

#                 for cornerPoint in pointXMap[x2]:

#                     if cornerPoint in pointsUsed:
#                         continue
#                     pointsUsed.add(cornerPoint)

#                     x3, y3 = cornerPoint

#                     desiredPoint = (x1, y3)

#                     if desiredPoint in (pointXMap[x1].intersection(pointYMap[y3])):

#                         validRectArea = self.calcArea(p1, matchingP1YPoint, desiredPoint, cornerPoint)

#                         if not bestArea:
#                             bestArea = validRectArea

#                         if validRectArea < bestArea:
#                             bestArea = validRectArea
        
#         return bestArea if bestArea else 0

#     def minAreaRect(self, points: List[List[int]]) -> int:
#         pass

# IDFK how this works
class Solution(object):
    def minAreaRect(self, points):
        columns = defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx = {}
        ans = float('inf')

        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1,y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0

if __name__ == "__main__":
    print(Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))
    print(Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))
    print(Solution().minAreaRect([[3,2],[3,1],[4,4],[1,1],[4,3],[0,3],[0,2],[4,0]]))
    print(Solution().minAreaRect([[3,2],[0,0],[3,3],[3,4],[4,4],[2,1],[4,3],[1,0],[4,1],[0,2]]))
                    
        
        
        