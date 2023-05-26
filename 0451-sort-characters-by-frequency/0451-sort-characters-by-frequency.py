class Solution:
    def frequencySort(self, s: str) -> str:
        return  list(chain(*[[x] * y for x, y in sorted(Counter(s).items(), key = lambda x : -x[1])])) 
        
            
        