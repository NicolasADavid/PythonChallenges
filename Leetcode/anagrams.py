from collections import Counter

def solution(array, target):

    ans = []

    c = Counter(target)

    for word in array:
        c2 = Counter(word)

        if c == c2:
            ans.append(word)

    return ans

assert solution(["cat", "tac", "tic", "act"], target = "tca") == ["cat", "tac", "act"]