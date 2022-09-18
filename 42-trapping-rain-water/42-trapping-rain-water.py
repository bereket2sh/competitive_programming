class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]*len(height)
        maxRight = [0]* len(height)
        minMaxLeftRight = [0] * len(height)
        
        for i in range(1,len(height)):
            maxLeft[i] = max(height[i-1], maxLeft[i-1])
        
        for i in range(len(height)-2 , -1, -1):
            maxRight[i] = max(height[i+1], maxRight[i+1])
        
        for i in range(len(height)):
            minMaxLeftRight[i] = min(maxLeft[i], maxRight[i])
            
        ans = 0
        for i in range(len(height)):
            temp = minMaxLeftRight[i] - height[i]
            if temp > 0:
                ans += temp
                
        return ans