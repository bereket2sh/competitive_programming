class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        #combining both plant time and grow in array as a 2d list
        plantGrow = list(zip(growTime, plantTime))
        
        #sort by higher number grow time first
        
        plantGrow.sort(key = lambda x : -x[0])
        
        currentPlantTime = 0
        result = 0
        
        for grow, plant in plantGrow:
            currentPlantTime += plant
            
            result  = max(result, grow + currentPlantTime)
            
        return result