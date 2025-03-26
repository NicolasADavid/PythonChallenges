
from typing import List
from collections import deque
def generate_permutations(s: str) -> List[str]:

    answers = set()
    callCount = 0
    ansCount = 0

    def helper(chosen, choices):

        nonlocal callCount
        nonlocal ansCount

        callCount += 1

        if len(chosen) == len(s):
            ansCount += 1
            answers.add(tuple(chosen))
            return
        
        subChoices = deque(choices)
        
        for _ in range(len(choices)):

            chosen.append(subChoices.popleft())
            helper(chosen, subChoices)
            subChoices.append(chosen.pop())
    
    helper([], [c for c in s])

    print(f"Call Count: {callCount}")
    print(f"Answer Count: {ansCount}")
    print(f"Dedup Answer Count: {len(answers)}")
        
    return [list(x) for x in answers]

answers = generate_permutations("abc")
for answer in answers:
    print(answer)





        
