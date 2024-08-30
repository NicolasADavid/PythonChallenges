'''
Frequency Stack

Implement a stack that returns the most frequent element when the pop() method is called instead of the last element added. In the event of a tie, pop the last element added into the stack.


EXAMPLE(S)
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].

EXPLORE



BRAINSTORM
- maintain the following:
    - mapping of each element to its frequency: 5 -> 1, 7 -> 1, 5 -> 2
    - mapping of frequencies to elements with that frequency: 1 -> [5], 1 -> [5, 7], 2 -> [5]
    - counter of max frequency: 1, 1, 2
    - to pop from stack: look at max frequency, pop the last value from that list: 2, 2 -> [5] so pop 5

PLAN
Init:
    - Initialize empty dicts to map frequencies to element lists and elements to frequencies
    - Initialize a counter to 0 to track the max frequency

Push:
    - Increase the frequency of this element
    - If this frequency is greater than the max frequency, update the latter
    - Append the element to the list for this frequency

Pop:
-If stack is empty, return None
-Pop from stack associated with highest frequency (freq-value map) (use maxFreq)
-Reduce frequency value associated with that element (value-freq map)
-Update highest frequency if stack associated with highest frequency is now empty (decrement maxFreq)
-Return element

'''
from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freqToValues = defaultdict(list)
        self.valueToFreq = defaultdict(int)
        self.maxFrequency = 0

    def pop(self) -> int:
        
        if self.maxFrequency == 0:
            return None
        
        element = self.freqToValues[self.maxFrequency].pop()

        self.valueToFreq[element] -= 1
        
        if len(self.freqToValues[self.maxFrequency]) == 0:
            self.maxFrequency -= 1
        
        return element

    def push(self, value) -> None:
        freq = self.valueToFreq[value] + 1
        self.valueToFreq[value] = freq
        self.maxFrequency = max(self.maxFrequency, freq)
        self.freqToValues[freq].append(value)

freqStack = FreqStack()
freqStack.push(5) # The stack is [5]
freqStack.push(7) # The stack is [5,7]
freqStack.push(5) # The stack is [5,7,5]
freqStack.push(7) # The stack is [5,7,5,7]
freqStack.push(4) # The stack is [5,7,5,7,4]
freqStack.push(5) # The stack is [5,7,5,7,4,5]
print(freqStack.pop())   # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
print(freqStack.pop())   # return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
print(freqStack.pop())   # return 5, as 5 is the most frequent. The stack becomes [5,7,4].
print(freqStack.pop())   # return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())