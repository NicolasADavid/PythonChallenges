def solution(matrix, k):
    
    n = len(matrix)
    m = len(matrix[0])
    
    if not m:
        return [[]]
    
    answer = [[0] * m for _ in range(n)]
    
    def valid(ir, ic):
        return ir >= 0 and ir < n and ic >= 0 and ic < m
    
    def help(ir, ic):
        
        t = 0
        
        sr = ir - k
        sc = ic - k
        
        for tr in range(sr, ir + 1 + k):
            for tc in range(sc, ic + 1 + k):
                if valid(tr, tc):
                    t += matrix[tr][tc]
                    
        return t
    
    for i in range(n):
        for j in range(m):
            new = help(i, j)
            answer[i][j] = new
    
    return answer
            

