class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2 != 0:
            return False
        op,cl,zero = 0,0,0
        for i in range(len(s)):
            if locked[i] == "0":
                zero += 1
            else:
                if s[i] == "(":
                    op += 1
                else:
                    cl += 1
            if cl > op + zero:
                return False
        op,cl,zero = 0,0,0
        for i in range(len(s)-1,-1,-1):
            if locked[i] == "0":
                zero += 1
            else:
                if s[i] == "(":
                    op += 1
                else:
                    cl += 1
            if op > cl + zero:
                return False
        return True
                