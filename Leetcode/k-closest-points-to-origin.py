from typing import List
class Solution:
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
    
print(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))