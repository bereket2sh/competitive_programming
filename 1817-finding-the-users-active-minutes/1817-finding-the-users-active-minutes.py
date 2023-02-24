class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = defaultdict(set)
        
        for i, time in logs:
            d[i].add(time)
            
        res = [0] * k
        
        for key, value in d.items():
            res[len(value) - 1] += 1
            
        return res