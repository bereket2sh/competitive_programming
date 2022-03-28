class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #space, time = O(n),O(n)
        
        res = set()
        store = set()
        window = len(s)-10+1  # for i in range window, s has atleast 10 elements
        
        for i in range(window):
            temp = "".join(s[i:10+i])
            
            if not store or temp not in store:
                store.add(temp)
            else:
                res.add(temp)
        return res
        
        

        