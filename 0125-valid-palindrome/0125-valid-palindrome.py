class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        
        for c  in s:
            if c.isalpha():
                newS += c.lower()
            elif c.isnumeric():
                newS += c               
        left, right = 0, len(newS) - 1
        
        while left < right:
            if newS[left] != newS[right]:
                return False
            left += 1
            right -= 1
            
        return True