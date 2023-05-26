class Solution:
    def frequencySort(self, s: str) -> str:
        s = Counter(s)
        
        ans = []
        s = sorted(s.items(), key = lambda x : -x[1])
        for x, y in s:
            ans.extend([x ] * y)
            
        return ans
        