class Solution:
    def frequencySort(self, s: str) -> str:
        s = Counter(list(s))
        ans, temp = [], []
        for key, val in s.items():
            temp.append([key, val])
            
        temp.sort(key = lambda x : -x[1])
        
        for a, b in temp:
            while b > 0:
                ans.append(a)
                b -= 1
                
        return ans