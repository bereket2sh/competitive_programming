class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        dic2 = {}
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] != t[i]:
                return False
            elif t[i] in dic2 and dic2[t[i]] != s[i]:
                return False
            
            else:
                dic[s[i]] = t[i]
                dic2[t[i]] = s[i]

        return True