class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        ind = 0
        
        while ind < len(gas):
            if gas[ind] >= cost[ind]:
                current_gas = gas[ind]
                travel = 0
                temp = ind
                
                
                while travel != len(gas):
                    current_gas -= cost[temp]
                    temp = (temp + 1) % len(gas)
                    if current_gas < 0:
                        break
                    
                    
                    current_gas += gas[temp]
                    travel += 1
                    
                if travel == len(gas):
                    return ind
            
                if temp <= ind:
                    return -1
                
                ind = temp
                
            else:
                ind += 1
                
            
        return -1            
                