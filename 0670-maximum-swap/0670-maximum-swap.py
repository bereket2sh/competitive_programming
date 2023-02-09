class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        
        count = 0
        
        i = 0
        while count == 0 and i < len(num):
            maxIndex = i
            for j in range(i + 1, len(num)):
                if int(num[j]) > int(num[maxIndex]):
                    maxIndex = j
                    
            if maxIndex != i:
                for h in range(len(num) - 1, i, -1):
                    if int(num[h]) == int(num[maxIndex]):
                        maxIndex = h
                        break
                count += 1
                num[i], num[maxIndex] = num[maxIndex], num[i]
                
            i += 1
            
        return int("".join(num))