def getLengthOfLongestChain(list):
    
    answer = []
    
    def help(list, i, build):
        
        nonlocal answer
        
        # check if valid situation
        if len(build) > 0:
            if len(build) > 1:
                
                # valid build
                if(build[-2] < build[-1]):
                    if len(answer) < len(build):
                        # print("Replace: ", answer, " with: ", build)
                        answer = build.copy()
                else:
                    # invalid build
                    # print("invalid: ", build)
                    return
            
            else:
                # valid build of 1
                if len(answer) < len(build):
                    answer = build.copy()
                    
        if i == len(list):
            return
        
        # add choice i to build
        build.append(list[i])
        help(list, i + 1, build)
        
        # remove choice i from build
        build.pop()
        
        help(list, i + 1, build)
        
    help(list, 0, [])
    
    return len(answer)

assert getLengthOfLongestChain([1, 2, 3, 4])              == 4 # -> 4  // [1, 2, 3, 4]
assert getLengthOfLongestChain([4, 3, 2, 1])              == 1 # -> 1  // [1], [2], [3], or [4]
assert getLengthOfLongestChain([1, 3, 2, 4])              == 3 # -> 3  // [1, 3, 4] or [1, 2, 4]
assert getLengthOfLongestChain([1, 3, 2, 4, 5, 8, 6, 7])  == 6 # -> 6  // [1, 2, 4, 5, 6, 7]
assert getLengthOfLongestChain([10, 2, 7, 3, 6, 1, 4, 5]) == 4 # -> 4  // [2, 3, 4, 5]