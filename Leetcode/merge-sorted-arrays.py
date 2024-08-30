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
        t = heapq.heappop(arrs)
        val = t[0]
        arr = t[1]

        output.append(val)

        if len(arr) > 1:
            heapq.heappush(arrs, (arr[1], arr[1:], tb))
            tb += 1

    return output






assert solution([[]]) == []
assert solution([[1,2]]) == [1,2]
assert solution([[1,2], [3]]) == [1,2,3]