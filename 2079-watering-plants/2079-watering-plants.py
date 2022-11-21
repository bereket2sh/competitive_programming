class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        result = 0
        p1 = 0
        tmp = capacity
        
        while p1 < len(plants):
            if plants[p1] <= tmp:
                result += 1
                tmp -= plants[p1]
                
            else:
                result += p1 + p1 + 1
                tmp = capacity - plants[p1]
                
            p1 += 1
            
        return result