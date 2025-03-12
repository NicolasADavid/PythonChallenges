'''
You are tasked with building a screen that shows the top games being played on a classic board game app. To prevent the games from jumping around on the screen, you must write a function with the following constraints:

Given two arrays, 'oldIDs' and 'newIDs', return an array that meets the following criteria:
- result contains all values from newIDs
- all new ids that currently exist in oldIDs are in the same index as they were in oldIDs
 

EXAMPLE(S)
oldIDs: [1, 2, 3]
newIDs: [2, 3, 4]
result: [4, 2, 3]

oldIDs: [1, 2, 3, 4]
newIDs: [4, 3, 2, 1]
result: [1, 2, 3, 4]

oldIDs: [1, 2, 3]
newIDs: [3, 4, 5]

result: [4, 5, 3] or [5, 4, 3]

oldIDs: [1, 2, 3]
newIDs: [3, 2, 1]
result: [1, 2, 3]
 

FUNCTION SIGNATURE
function preserveIndices(oldIDs: [string], newIDs: [string]) => result: [string]


Explore
- always given old and new ids
- incase new ids does not match any id in old id in then we can return new ids
- both lists are fixed size to each other
- no duplicates


Brainstorming

Carlo
- converting newIds to set,
- iterate through oldID
  - if current id is in set
    - delete id from set
    - move to the next index
  - if current id is not in set
    - add index to a list

after iteration of old Id, we have
  - list of index needed to be replaced
  - set of numbers that can be placed
iterate for range 0 -> lenghth of list O(n)
  oldId[ list[i] ] = set[i] O(n)

return oldId array (in place)



Rav TO(m+n) / 2 passes
- converting newIds to set,
- result that is fixed size
- iterate through oldID array (preserve order)
  - if current id is in set --> new Id set
    - fill in our result array with that id
    - delete id from set
- traverse through our newIdset --> what is remaining needs to be filled in result
    - while our result is not undefined -> we skip
    - when we are at an undefined result --> we add that id to that undefined spot
- return the result



Nico

### Dict/map
- map through oldIds -> map[id] -> idx
- create newList =  [None] * len(oldIds)
- create tmpList = []
- map through newIds
  - if newId in map
    - newList[map[newId]] = newId
  - else
    - insert tmpList
  
  map through every index of newList
  - if None
    - insert(tmpList.pop())
  - else
    - continue
  
  return newList
  
### Set

newSet = set(newIds)
oldSet = set(oldIds)

nextUnseenIdx = -1

def advance()
  nextUnseenIdx += 1
  while nextUnseenIdx < len(newIds) and newIds[nextUn] not in oldSet:
    nextUnseenIdx += 1

advance()

iterate through oldIds O(N)
  if element not in newSet
    oldIds[idx] = newIds[nextUnseenIdx]
    advance(nextUnseenIdx) 
  else
    continue
  
  return oldIds


'''

from typing import List
def preserveIndices(oldIDs: List[str], newIDs: List[str]) -> List[str]:

  idxs = {}

  for idx, el in enumerate(oldIDs):
    idxs[el] = idx

  newSet = [None] * len(oldIDs)
  tmpSet = []

  for el in newIDs:
    if el in idxs:
      newSet[idxs[el]] = el
    else:
      tmpSet.append(el)

  for idx in range(len(newSet)):
    if newSet[idx] is None:
      newSet[idx] = tmpSet.pop()
  
  return newSet

# print("Test 1")
# assert preserveIndices(oldIDs = [1, 2, 3], newIDs = [2, 3, 4]) == [4, 2, 3]
# print("Test 2")
# assert preserveIndices(oldIDs = [1, 2, 3, 4], newIDs = [4, 3, 2, 1]) == [1, 2, 3, 4]
# print("Test 3")
# assert preserveIndices(oldIDs = [1, 2, 3], newIDs = [3, 4, 5]) == [5, 4, 3]
# print("Test 4")
# assert preserveIndices(oldIDs = [1, 2, 3], newIDs = [3, 2, 1]) == [1, 2, 3]


"""
- newIdsset = set(newIDs)

oldID [ 1 , 2 , 3 ]
newIDs[ 2, 3. , 4 ]
result []
- loop 1: iterate over oldIds, 
          if(oldIOds[i] is not in newID)
            result.push(undefined)
          else
            result.push(oldIds[i])
            newId.delete(oldId[i])

   
result [undefined, 2 , 3 ] 
newIds = [4]


loop 2: Iterate over result, keep on adding newIDs.pop() for each undefined.


result [4, 2 , 3 ] 
newIds = []"
"""

from typing import List
def preserveIndicesSet(oldIDs: List[str], newIDs: List[str]) -> List[str]:
    newSet = set(newIDs)
    newList = []
    for idx, el in enumerate(oldIDs):
        if el in newSet:
            newList.append(el)
            newSet.remove(el)
        else:
            newList.append(None)
    remainingIds = list(newSet)

    for idx, el in enumerate(newList):
      if el is None:
        newList[idx] = remainingIds.pop()
    
    return newList
  
print("Test 1")
assert preserveIndicesSet(oldIDs = [1, 2, 3], newIDs = [2, 3, 4]) == [4, 2, 3]
print("Test 2")
assert preserveIndicesSet(oldIDs = [1, 2, 3, 4], newIDs = [4, 3, 2, 1]) == [1, 2, 3, 4]
print("Test 3")
assert preserveIndicesSet(oldIDs = [1, 2, 3], newIDs = [3, 4, 5]) == [5, 4, 3]
print("Test 4")
assert preserveIndicesSet(oldIDs = [1, 2, 3], newIDs = [3, 2, 1]) == [1, 2, 3]

# Takeaway : If the indexs in an array are important, try to traverse that, so that you dont need to store it in a map
