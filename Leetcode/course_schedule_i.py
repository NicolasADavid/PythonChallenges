'''
You are given an integer numCourses representing the total number of courses you would like to take, labeled from 0 to numCourses − 1. You are also given an array prerequisites where each element is a pair [a, b] that denotes you must complete course b before course a.

Return true if it is possible to finish every course under the prerequisite constraints; otherwise, return false.

Assumptions:
• 0 ≤ numCourses ≤ 100 000
• 0 ≤ prerequisites.length ≤ 200 000
• prerequisites may contain duplicate pairs.

Design an algorithm that works for large inputs.
 

EXAMPLE(S)
Input:
numCourses = 2
prerequisites = [[1,0]]
Output: true
Explanation: Take course 0 first, then course 1.

Input:
numCourses = 2
prerequisites = [[1,0],[0,1]]
Output: false
Explanation: The two courses depend on each other, forming a cycle.
 
Input
numCourses = 3
prerequisites = [[1,0],[2,1],[3,2]]
Output: false

numCourses = 8
prerequisites = [[1,0],[2,1],[3,2], [5,4], [7,6],]
Output: true

numCourses = 8
prerequisites = [[1,0],[2,1],[3,0]]
Output: true

numCourses = 8
prerequisites = [[1,0],[2,1],[3,0],[0, 2]]
Output: false

numCourses = 7
prerequisites = [[1,0],[2, 1],[3,2],[4,0],[5,0],[6,0]]]
Output: true


prereq = {} course -> set of prereqs
course = 0

1 new pair
    if first course not seen before, course += 1, init prereq set
    if second course not seen before, course += 1, init prereq set
    add second course and its prereqs to prereqs of first course
    check no cycle

return true if total courses <= num courses

FUNCTION SIGNATURE
function canFinish(numCourses, prerequisites)
'''
from collections import defaultdict
def canFinish(numCourses, prerequisites) -> bool:

    prereqs = defaultdict(set)
    total = 0

    for [a, b] in prerequisites:
        if a not in prereqs:
            total += 1
        if b not in prereqs:
            total += 1
        
        prereqs[a].add(b)
        # prereqs[a] += prereqs[b] 
        prereqs[a] = prereqs[a].union(prereqs[b])

        if a in prereqs[a]:
            return False
    
    return total <= numCourses

numCourses = 2
prerequisites = [[1,0]]
assert canFinish(numCourses, prerequisites)

numCourses = 2
prerequisites = [[1,0],[0,1]]
assert not canFinish(numCourses, prerequisites)

numCourses = 3
prerequisites = [[1,0],[2,1],[3,2]]
assert not canFinish(numCourses, prerequisites)

numCourses = 8
prerequisites = [[1,0],[2,1],[3,2], [5,4], [7,6],]
assert canFinish(numCourses, prerequisites)

numCourses = 8
prerequisites = [[1,0],[2,1],[3,0]]
assert canFinish(numCourses, prerequisites)

numCourses = 8
prerequisites = [[1,0],[2,1],[3,0],[0, 2]]
assert not canFinish(numCourses, prerequisites)

numCourses = 7
prerequisites = [[1,0],[2, 1],[3,2],[4,0],[5,0],[6,0]]
assert canFinish(numCourses, prerequisites)


###### FORMATION ANSWER ######
from collections import defaultdict, deque
from typing import List

# Time  : O(V + E)
# Space : O(V + E)

def canFinishF(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Build graph and indegree array
    adj = defaultdict(list)           # course -> list of courses unlocked after it
    indeg = [0] * numCourses          # number of unmet prerequisites for each course

    for a, b in prerequisites:
        adj[b].append(a)
        if a >= numCourses:
            return False
        indeg[a] += 1

    # Start with all courses that have no prerequisites
    queue = deque([c for c in range(numCourses) if indeg[c] == 0])
    visited = 0                       # number of courses we managed to "take"

    while queue:
        course = queue.popleft()
        # print("took: ", course)
        # print('\n')
        visited += 1
        for nxt in adj[course]:
            indeg[nxt] -= 1           # one prerequisite satisfied
            if indeg[nxt] == 0:
                queue.append(nxt)
    # print("visited ", visited)
    return visited == numCourses

# numCourses = 2
# prerequisites = [[1,0]]
# assert canFinishF(numCourses, prerequisites) == True

# numCourses = 2
# prerequisites = [[1,0],[0,1]]
# assert canFinishF(numCourses, prerequisites) == False

numCourses = 3
prerequisites = [[1,0],[2,1],[3,2]]
assert not canFinishF(numCourses, prerequisites)

numCourses = 4
prerequisites = [[1,0],[2,1],[3,2]]
assert canFinishF(numCourses, prerequisites)

numCourses = 8
prerequisites = [[1,0],[2,1],[3,2], [5,4], [7,6],]
assert canFinishF(numCourses, prerequisites)

numCourses = 8
prerequisites = [[1,0],[2,1],[3,0]]
assert canFinishF(numCourses, prerequisites)

numCourses = 8
prerequisites = [[1,0],[2,1],[3,0],[0, 2]]
assert not canFinishF(numCourses, prerequisites)

numCourses = 7
prerequisites = [[1,0],[2, 1],[3,2],[4,0],[5,0],[6,0]]
assert canFinishF(numCourses, prerequisites)

'''
[[1,0],[0,1]] => cycle
prereq
{
  1: [0]
  0: [1]
}
indegree = [1,1]

numCourse = 4
[1,0],[2,1],[3,2],[0,3],[9,0],[6,0],[4,5],[7,8] => cycle
prereq

{
  1: [0]
  2: [1]
  3: [2]
  0: [3]
}
indegree = [1,1,1,1]

'''

numCourses = 10
prerequisites = [[1,0],[2,1],[3,2],[0,3],[9,0],[6,0],[4,5],[7,8]]
assert not canFinish(numCourses, prerequisites)
assert not canFinishF(numCourses, prerequisites)