class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        
        for i in range(len(tasks)):
            tasks[i].append(i)
            
        tasks.sort()
        
        cur_time = 0
        
        ans = []
        ind = 0
        current = []
        
        while ind < len(tasks):
            
            
            while ind < len(tasks):
                
                if tasks[ind][0] <= cur_time:
                    heappush(current, [tasks[ind][1], tasks[ind][-1] , tasks[ind][0]])
                    ind += 1
                else:
                    break
            # print(current) 
            if current:
                temp = heappop(current)
                ans.append(temp[1])
                
                cur_time += temp[0]
            else:
                cur_time = tasks[ind][0]
        while current:
            temp = heappop(current)
            ans.append(temp[1])
            
        return ans
                
        
        
        
        
        