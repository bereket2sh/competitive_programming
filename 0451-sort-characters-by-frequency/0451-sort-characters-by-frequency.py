class Solution:
    def frequencySort(self, s: str) -> str:
        # you won't understand my code :)
        # return  list(chain(*[[x] * y for x, y in sorted(Counter(s).items(), key = lambda x : -x[1])])) 
        
        cnt = Counter(s)
        n = len(s)
        bucket = [[] for _ in range(n+1)]
        for c, freq in cnt.items():
            bucket[freq].append(c)
        
        ans = []
        for freq in range(n, -1, -1):
            for char in bucket[freq]:
                ans.extend([char] * freq)
        return "".join(ans)
        
            
        