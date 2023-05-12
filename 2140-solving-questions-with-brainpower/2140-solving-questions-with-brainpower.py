class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @cache
        def dp(index):
            if index >= len(questions):
                return 0
            
            
            ans = max((questions[index][0] + dp(index + 1 + questions[index][1])), (dp(index + 1)))
            return ans
        
        return dp(0)
            