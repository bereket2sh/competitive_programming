class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        left = [0]
        right = [0]
        res = []
        for i in range(1,len(security)):
            if security[i] <= security[i-1]:
                left.append(left[-1]+1)
            else:
                left.append(0)
        for i in range(len(security)-2,-1,-1):
            if security[i] <= security[i+1]:
                right.append(right[-1]+1)
            else:
                right.append(0)
        right.reverse()
        for i in range(time,len(security)-time):
            if right[i] >= time and left[i] >= time:
                res.append(i)
        return res
            
