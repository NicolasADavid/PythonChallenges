'''
❓ PROMPT
Given an array, find the length of the smallest subarray in it which, when sorted, will sort the whole array.

Example(s)
Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted.

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted.
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function shortestWindowSort(arr) {
def shortestWindowSort(arr: list[int]) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def shortestWindowSort(arr: list[int]) -> int:
    if not arr:
        return 0
    
    n = len(arr)
    l = 0
    r = len(arr) - 1

    if n == 0 or n == 1:
        return 0

    # is sorted?
    f = True
    for i in range(1, n):
        if arr[i-1] > arr[i]:
            f = False

    if f:
        return 0

    # find first OOO L->R
    while l < n - 1 and arr[l] <= arr[l+1]:
        l += 1

    # find first OOO R->L
    while r > 1 and arr[r] >= arr[r-1]:
        r -= 1

    # find max in window
    wmax = float("-inf")
    for i in range(l, r+1):
        wmax = max(wmax, arr[i])

    # find min in window
    wmin = float("inf")
    for i in range(l, r+1):
        wmin = min(wmin, arr[i])

    # expand left until bound or arr[l-1] <= window min
    while l > 0 and wmin < arr[l - 1]:
        l -= 1

    # expand right until bound or arr[r+1] >= window min
    while r < n - 1 and wmax > arr[r + 1]:
        r += 1

    return r - l + 1

assert shortestWindowSort([1, 2, 5, 3, 7, 10, 9, 12]) == 5  # [5, 3, 7, 10, 9]
assert shortestWindowSort([1, 3, 2, 0, -1, 7, 10]) == 5     # [1, 3, 2, 0, -1]

# null or empty
assert shortestWindowSort([]) == 0

# 1-element
assert shortestWindowSort([1]) == 0

# 2 adjacent elements are unsorted
assert shortestWindowSort([1, 2, 5, 4, 6, 7]) == 2

# 2 distant elements are unsorted
assert shortestWindowSort([10, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 10

# N-element unsorted array
assert shortestWindowSort([7,6,5,4,3,2,1]) == 7

# sorted array
assert shortestWindowSort([1, 2, 3, 4, 5, 6]) == 0
