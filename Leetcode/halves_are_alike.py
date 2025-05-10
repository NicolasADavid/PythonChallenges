class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        half = len(s) // 2

        vowels = set([c for c in "aeiouAEIOU"])

        a = s[:half]
        ac = sum([1 for x in a if x in vowels])
        
        b = s[half:]
        bc = sum([1 for x in b if x in vowels])

        return ac == bc