# function basicDynamicProgrammingPattern(/* parameters */) {
#  // Create table

#  // Fill in initial table values from recursive base cases

#  // for each cell in the table
#    // compute new cells value based on previous values

#   // return desired cell
# }

def fibdp(n):

    if n == 0:
        return 0
    
    #  // Create table
    dp = [-1] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(fibdp(0))
print(fibdp(1))
print(fibdp(2))
print(fibdp(3))
print(fibdp(4))
print(fibdp(5))
#  // Fill in initial table values from recursive base cases

#  // for each cell in the table
#    // compute new cells value based on previous values

#   // return desired cell