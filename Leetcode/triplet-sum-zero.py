#  Given an array of integers, find a triplet (a, b, c) that their sum equals zero (a + b + c = 0).

# In case there are multiple such triplets, return one sorted triplet with the smallest value

def solution(array):

    n = len(array)
    if n < 3:
        return []
    
    best = float('inf')
    ans = []

    for idx, target in enumerate(array):

        # find complement of target in the sum of two elements in rest of the array:
        for j in range(idx + 1, n):
            for k in range(j + 1, n):
                je = array[j]
                ke = array[k]

                if je + ke == - target:

                    mini = min([target, ke, je])

                    if best > mini:
                        best = mini
                        ans = [target, ke, je]
                        ans.sort()

    return ans

assert solution([1, 2, 0]) == []
assert solution([-1, 0, 1, 0, 1]) == [-1, 0, 1]
assert solution([-5, -1, 0, 1, 4, -1]) == [-5,1,4]