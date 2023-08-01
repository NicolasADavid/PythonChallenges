from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        sc = Counter(s)
        tc = Counter(t)

        sc.subtract(tc)
        
        for value in sc.values():
            if value != 0:
                return False
            
        return True
    
# print(Solution().isAnagram("aba", "baa"))
print(Solution().isAnagram("car", "rat"))