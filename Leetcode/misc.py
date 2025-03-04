def solution(array):
    
    ans = []
    
    for i, num in enumerate(array):
        
        if (i+1) % 2 == 1 and num % 2 == 1:
            continue
        
        ans.append(num)
        
    return ans

# print(solution([1,2,3]))


def printChess():
    for i in range(8):
        p = []
        for j in range(8):
            if i == j:
                p.append(" X ")
            else:
                p.append(" _ ")
        
        print("".join(p))

printChess()

#  _  _  _  _  _  _  _  _ 
#  _  _  _  _  _  _  _  _ 
#  _  _  _  _  _  _  _  _ 
#  _  _  _  _  _  _  _  _ 
#  _  _  _  _  _  _  _  _ 
#  _  _  _  _  _  _  _  _ 
#  _  _  _  _  _  _  _  _ 
#  _  _  _  _  _  _  _  _



#  X  _  _  _  _  _  _  _ 
#  _  X  _  _  _  _  _  _ 
#  _  _  X  _  _  _  _  _ 
#  _  _  _  X  _  _  _  _ 
#  _  _  _  _  X  _  _  _ 
#  _  _  _  _  _  X  _  _ 
#  _  _  _  _  _  _  X  _ 
#  _  _  _  _  _  _  _  X 
