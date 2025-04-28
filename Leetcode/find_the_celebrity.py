"""

277. Find the Celebrity

Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given an integer n and a helper function bool knows(a, b) that tells you whether a knows b. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.

Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.

Note that the n x n 2D array graph given as input is not directly available to you, and instead only accessible through the helper function knows. graph[i][j] == 1 represents person i knows person j, wherease graph[i][j] == 0 represents person j does not know person i.



Example 1:

Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1

Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
Example 2:


Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.

"""


# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

def knows(a, b):
    # This is a mock implementation for the purpose of this example.
    # In a real scenario, this function would be provided by the system.
    g = [[1,0,1],[1,1,0],[0,1,1]]

    return True if g[a][b] == 1 else False

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """

        celebrity = 0
        idx = 1
        while idx < n:
            if knows(celebrity, idx):
                celebrity = idx
            idx += 1
        
        # Ensure that the celebrity does not know anyone else
        for i in range(n):
            if i != celebrity and knows(celebrity, i):
                return -1
                
        # Ensure that everyone knows the celebrity
        for i in range(n):
            if i != celebrity and not knows(i, celebrity):
                return -1
            
        return celebrity
    
print(Solution().findCelebrity(3))
