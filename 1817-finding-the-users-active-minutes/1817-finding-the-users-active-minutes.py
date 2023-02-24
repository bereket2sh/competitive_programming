class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = defaultdict(set)
        
        for i, time in logs:
            d[i].add(time)
            
        d2 = defaultdict(int)
        
        for key, value in d.items():
            d2[len(value)] += 1
            
        res = [0] * k
        
        for i in range(k):
            res[i] = d2[i + 1]
            
        return res