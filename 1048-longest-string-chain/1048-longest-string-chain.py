class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        s = set(words)
        
        memo = {}
        
        def recursive(word):
            if word not in s:
                return 0
            if word in memo:
                return memo[word]
            
            else:
                mx = 0
                
                for i in range(len(word)):
                    mx = max(mx, recursive(word[:i] + word[i + 1: ]) + 1)
                    
                memo[word] = mx
                
                return mx
            
        for w in words:
            recursive(w)
            
        return max(memo.values())