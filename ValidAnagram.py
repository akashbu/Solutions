
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)    
        counterS = {}
        counterT = {}

        if len(s) != len(t):
            return False

        for i in range(0, len(s)):
            counterS[s[i]] = 1+ counterS.get(s[i],0)
            counterT[t[i]] = 1+ counterT.get(t[i],0)
        
        for c in counterS:
            if counterS[c] != counterT.get(c,0):
                return False
        
        return True