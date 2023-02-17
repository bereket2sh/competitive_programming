class Solution:
    def firstUniqChar(self, s: str) -> int:
        tmp = Counter(s)

        for i in range(len(s)):
            if tmp[s[i]] == 1:
                return i

        return -1 

             