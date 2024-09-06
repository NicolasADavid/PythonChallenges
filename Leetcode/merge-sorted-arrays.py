import heapq

def solution(m):

    arrs = []

    tb = 0

    for array in m:
        if array:
            heapq.heappush(arrs, (array[0], array, tb))
            tb += 1

    output = []
    
    while arrs:
        (val, arr, _) = heapq.heappop(arrs)
        val = t[0]
        arr = t[1]

        output.append(val)

        if len(arr) > 1:
            heapq.heappush(arrs, (arr[1], arr[1:], tb))
            tb += 1

    return output






assert solution([[]]) == []
assert solution([[1,2]]) == [1,2]
assert solution([[1,2], [3], [5,6],[1,2,3,4,5]]) == [1,1,2,2,3,3,4,5,5,6]