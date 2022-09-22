class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            word = list(s[i])
            word.reverse()
            word = "".join(word)
            s[i] = word
        
        return " ".join(s)