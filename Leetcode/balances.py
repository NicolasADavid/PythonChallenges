def solution(balances, requests):
    
    for i, request in enumerate([r.split() for r in requests]):
        
        request = [request[0]] + [int(x) for x in request[1:]]
        
        action = request[0]
        
        def errval():
            return [-(i+1)]
        
        match action:

            case "deposit":
                # check validity
                # account exists
                if request[1]-1 >= len(balances):
                    return errval()
                
                # operate
                balances[request[1]-1] += request[2]
            
            case "withdraw":
                # check validity

                # account exists
                if request[1]-1 >= len(balances):
                    return errval()
                
                # balance is not exceeded
                if balances[request[1]-1] < request[2]:
                    return errval()
                
                # operate
                balances[request[1]-1] -= request[2]
                
            case "transfer":
                # check validity
                # account 1 exists
                if request[1] - 1 >= len(balances):
                    return errval()
                # account 2 exists
                if request[2] - 1 >= len(balances):
                    return errval()
                # account1 balance is not exceeded
                if balances[request[1]-1] < request[3]:
                    return errval()
                
                # operate
                balances[request[1]-1] -= request[3]
                balances[request[2]-1] += request[3]
    
    return balances

# print(solution(balances = [10, 100, 20, 50, 30], requests =["withdraw 2 10", "transfer 5 1 20", "deposit 5 20", "transfer 3 4 15"]))
print(solution([42], ["transfer 1 2 3"]))


