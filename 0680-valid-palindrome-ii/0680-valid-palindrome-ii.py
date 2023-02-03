class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            l = s[left : right]
            r = s[(left + 1) : (right + 1)]
            
            if s[left] != s[right]:
                if l == l[::-1] or r == r[::-1]:
                    return True
                return False
            left += 1
            right -= 1
            
        return True