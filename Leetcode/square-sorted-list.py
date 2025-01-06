
from collections import deque

def solution(array):

    if not array:
        return []

    negatives = deque()

    positives = deque(array)

    while positives and positives[0] < 0:
        negatives.appendleft(positives.popleft())

    answer = []

    while negatives and positives:
        n = negatives[0]
        p = positives[0]
        if abs(n) <= p:
            answer.append(n * n)
            negatives.popleft()
        else:
            answer.append(p * p)
            positives.popleft()
    
    while negatives:
        n = negatives[0]
        answer.append(n * n)
        negatives.popleft()
        
    while positives:
        p = positives[0]
        answer.append(p * p)
        positives.popleft()

    return answer

print(solution([-7, -3, -2, 2, 3, 11]))
# [-7, -3, -2, 2, 3, 11]
# [4, 4, 9, 9, 49, 121]