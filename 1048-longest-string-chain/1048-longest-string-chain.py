class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        chain = defaultdict(list)
        
        for i in range(len(words)):
            for j in range(len(words)):
                if len(words[j]) == len(words[i]) + 1 and self.isChain(words[i], words[j]):
                    chain[words[i]].append(words[j])
                    
        self.ans = [1]
        
        @cache
        def dfs(node, count):
            if not chain[node]:
                self.ans.append(count)
                return 
            
            for child in chain[node]:
                dfs(child, count + 1)
              
        for key in list(chain):
            dfs(key, 1)
            
        return max(self.ans)
            
                    
                    
    def isChain(self, word1, word2):
        for i in range(len(word2)):
            if word1 == word2[:i] + word2[i + 1: ]:
                return True
            
        return False

      