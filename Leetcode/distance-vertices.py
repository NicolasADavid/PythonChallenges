def solution(matrix, vertex1, vertex2):

    # Start from vertex 1

    # Travel to neighbors, passing steps

    # If at vertex 2, track best

    neighbors = [(x, 1) for x, val in enumerate(matrix[vertex1]) if val == True]

    seen = set()
    best = float('inf')

    distances = {}

    while neighbors:

        (n, dist) = neighbors.pop()

        if n not in distances:
            distances[n] = float('inf')

        if distances[n] < dist:
            continue
        distances[n] = dist

        if n == vertex2:
            best = min(best, dist)
        else:
            for newN, val in enumerate(matrix[n]):
                if val:
                    neighbors.append((newN, dist+1))      

    return best

# print(solution([[False, False, True],
#           [False, False, True],
#           [True, True, False]], 0, 1))


print(solution([
    [False,True,False,False], 
    [True,False,True,True], 
    [False,True,False,True], 
    [False,True,True,False]],
    2,
    0))
