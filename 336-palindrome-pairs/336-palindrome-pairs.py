class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d = {}
        for i, w in enumerate(words):
          d[w[::-1]] = i
        indices = set()
        for i, w in enumerate(words):
          for j in range(len(w) + 1):
            prefix = w[:j]
            postfix = w[j:]
            if prefix in d and i != d[prefix] and postfix == postfix[::-1]:
              indices.add((i, d[prefix]))
            if postfix in d and i != d[postfix] and prefix == prefix[::-1]:
              indices.add((d[postfix], i))
        
        return [list(p) for p in indices]