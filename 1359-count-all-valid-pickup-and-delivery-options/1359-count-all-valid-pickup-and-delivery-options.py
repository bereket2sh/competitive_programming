class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        ans = self.countOrders(n-1)* (n * (2*n-1))
        return ans % (10**9+7)
        
        
        
        
        
        
        
        
        
        
        
        
        
#         mod = 10**9+7
#         current = 1 # intialy when n == 1
#         for i in range(2,n+1):
#             gaps = i*2-1
#             ways = gaps * (gaps+1)//2  #this give the sum from 1 to gaps  gaps is the num of possible pos
#             current *= ways
            
        
#         return current % mod