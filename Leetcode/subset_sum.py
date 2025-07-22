
'''

Given a set of numbers S, and a sum K, write a function to compute whether there exists a subset of S whose elements add up to K.

Each element of S is unique and may only be used once in computing the sum.

Example(s)
doesSubsetSumExist([1,2,3], 6) == true (1+2+3=6)
doesSubsetSumExist([1,2,3], 5) == true (2+3=5)
doesSubsetSumExist([1,2,9], 4) == false (no sum exists)


def does_subset_sum_exist(nums: list[int], sum: int) -> bool:


'''

# 1) recursive
# 2) top-down with memoization
# 3) bottom-up dynamic programming
# 4) space optimized dynamic programming


# Approach 1

# def isSubsetSumRec(arr, n, sum):
  
#     # Base Cases
#     if sum == 0:
#         return True 
#     if n == 0:
#         return False

#     # If the last element is greater
#     # than the sum, ignore it
#     if arr[n - 1] > sum:
#         return isSubsetSumRec(arr, n - 1, sum)

#     # Check if sum can be obtained by including
#     # or excluding the last element
#     return (isSubsetSumRec(arr, n - 1, sum) or 
#             isSubsetSumRec(arr, n - 1, sum - arr[n - 1]))

# def isSubsetSum(arr, sum):
#     return isSubsetSumRec(arr, len(arr), sum)

# if __name__ == "__main__":
  
#     arr = [3, 34, 4, 12, 5, 2]
#     sum = 9

#     if isSubsetSum(arr, sum):
#         print("True")
#     else:
#         print("False")

# Approach 2
# def isSubsetSumRec(arr, n, sum, memo):

#     # If the sum is zero, we found 
#     # a subset
#     if sum == 0:
#         return True

#     # If no elements are left
#     if n <= 0:
#         return False

#     # If the value is already 
#     # computed, return it
#     if memo[n][sum] != -1:
#         return memo[n][sum]

#     # If the last element is greater 
#     # than the sum, ignore it
#     if arr[n - 1] > sum:
#         memo[n][sum] = isSubsetSumRec(arr, n - 1, sum, memo)
#     else:
      
#         # Include or exclude the last element
#         # directly
#         memo[n][sum] = (isSubsetSumRec(arr, n - 1, sum, memo)
#                         or isSubsetSumRec(arr, n - 1, sum - arr[n - 1], memo))

#     return memo[n][sum]


# def isSubsetSum(arr, sum):
#     n = len(arr)
#     memo = [[-1 for _ in range(sum + 1)] for _ in range(n + 1)]
#     return isSubsetSumRec(arr, n, sum, memo)


# if __name__ == "__main__":
#     arr = [1, 5, 3, 7, 4]
#     sum = 12

#     if isSubsetSum(arr, sum):
#         print("True")
#     else:
#         print("False")

# Approach 3
def isSubsetSum(arr, sum):
    n = len(arr)

    # Create a 2D list for storing 
    # results of subproblems
    dp = [[False] * (sum + 1) for _ in range(n + 1)]

    # If sum is 0, then answer is 
    # true (empty subset)
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the dp table in bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < arr[i - 1]:
                
                # Exclude the current element
                dp[i][j] = dp[i - 1][j]
            else:
                
                # Include or exclude
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    return dp[n][sum]


if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    sum_value = 9

    if isSubsetSum(arr, sum_value):
        print("True")
    else:
        print("False")

# Approach 4
def isSubsetSum(arr, sum):
    n = len(arr)
    prev = [False] * (sum + 1)
    curr = [False] * (sum + 1)

    # Base case: sum 0 can always 
    # be achieved
    prev[0] = True

    # Fill the dp table in a
    # bottom-up manner
    for i in range(1, n + 1):
        for j in range(sum + 1):
            if j < arr[i - 1]:
                curr[j] = prev[j]
            else:
                curr[j] = prev[j] or prev[j - arr[i - 1]]
        prev = curr.copy() 

    return prev[sum]

if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    sum_value = 9
    if isSubsetSum(arr, sum_value):
        print("True")
    else:
        print("False")



# Execute
def does_subset_sum_exist(nums: list[int], target: int) -> bool:
    n = len(nums)
    dp = [[False] * (target +1) for _ in range(n+1)]

    for i in range(n + 1):
        dp[i][0] = True

    # For every row and column
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # If the current number is greater than the target
            if nums[i - 1] > j:
                # Do not include the number in the subset
                dp[i][j] = dp[i-1][j]
            else:
                # Either include the number or not
                dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i - 1]]
    
    return dp[n][target]
