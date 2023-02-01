class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        scoreAge = list(zip(scores, ages))
        
        scoreAge.sort()
        
        dp = sorted(scores)
        
        
        for i in range(len(scoreAge)):
            curScore, curAge = scoreAge[i]
            
            for j in range(i):
                score, age = scoreAge[j]
                
                if curAge >= age:
                    dp[i] = max(dp[i], dp[j] + curScore)
                    
        return max(dp)
        