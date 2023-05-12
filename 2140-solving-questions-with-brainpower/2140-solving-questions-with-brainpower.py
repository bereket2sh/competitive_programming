class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        memo = defaultdict(list)
        def dp(index):
            if index >= len(questions):
                return 0
            if index in memo:
                return memo[index]
            
            memo[index] = max((questions[index][0] + dp(index + 1 + questions[index][1])), (dp(index + 1)))
            return  memo[index]
        
        return dp(0)
            