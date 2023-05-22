class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if (sum(gas) - sum(cost)) < 0 : return -1
        
        total = 0
        start = 0
        for i in range(0, len(gas)):
            
            total += (gas[i] - cost[i])
            
            # reset
            if total < 0:
                start = i+1
                total = 0
            
        
        
        return start        