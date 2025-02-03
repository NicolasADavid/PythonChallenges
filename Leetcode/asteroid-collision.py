class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        outLeft = []
        movingRight = []

        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                movingRight.append(asteroids[i])
            else:

                destroyed = False

                #destroy asteroids in movingRight
                while movingRight and movingRight[-1] < abs(asteroids[i]):
                    movingRight.pop()

                if movingRight:
                    if movingRight[-1] > abs(asteroids[i]):
                        continue
                    else:
                        movingRight.pop()
                        destroyed = True
                
                if not destroyed:
                    outLeft.append(asteroids[i])

        return outLeft + movingRight
    
assert Solution().asteroidCollision([5, 10, -5]) == [5, 10]
assert Solution().asteroidCollision([8, -8]) == []
assert Solution().asteroidCollision([10, 2, -5]) == [10]