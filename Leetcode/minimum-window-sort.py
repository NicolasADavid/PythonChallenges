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
Time: O(N)
Space: O(1)
 

📆 PLAN
Outline of algorithm #: 
# is sorted?
# find first OOO L->R O(N)
# find first OOO R->L O(N)
# find max in window O(N)
# find min in window O(N)
# expand left until bound or arr[l-1] <= window min O(N)
# expand right until bound or arr[r+1] >= window min O(N)
return r - l + 1
 

🛠️ IMPLEMENT
function shortestWindowSort(arr) {
def shortestWindowSort(arr: list[int]) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def shortestWindowSort(arr: list[int]) -> int:
    n = len(arr)

    if n == 0 or n == 1:
        return 0

    l = 0
    r = len(arr) - 1
    
    # find first OOO L->R
    while l < n - 1 and arr[l] <= arr[l+1]:
        l += 1

    if l == len(arr) - 1:  # if the array is sorted
      return 0

    # find first OOO R->L
    while r > 1 and arr[r] >= arr[r-1]:
        r -= 1

    # find min + max in window
    window_max = float("-inf")
    window_min = float("inf")
    for i in range(l, r+1):
        window_max = max(window_max, arr[i])
        window_min = min(window_min, arr[i])

    # expand left until bound or arr[l-1] <= window min
    while l > 0 and window_min < arr[l - 1]:
        l -= 1

    # expand right until bound or arr[r+1] >= window min
    while r < n - 1 and window_max > arr[r + 1]:
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
