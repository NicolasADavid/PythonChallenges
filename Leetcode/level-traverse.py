from collections import deque

def solution(root):
    
    ans = []
    q = deque([root])
    
    
    while q:
        level = []
        for _ in range(len(q)):
            n = q.popleft()
            level.append(n.value)
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
            
        ans.append(level)
    
    return ans