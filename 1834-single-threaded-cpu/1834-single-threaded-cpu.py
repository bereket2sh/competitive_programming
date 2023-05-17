class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i in range(len(tasks)):
            tasks[i].append(i)
            
        heapify(tasks)
        
        cur_time = 0
        
        ans = []
        current = []
        
        while tasks:
            
            
            while tasks:
                
                if tasks[0][0] <= cur_time:
                    task = heappop(tasks)
                    heappush(current, [task[1], task[-1] , task[0]])
                else:
                    break

            if current:
                temp = heappop(current)
                ans.append(temp[1])
                
                cur_time += temp[0]
            else:
                cur_time = tasks[0][0]
        while current:
            temp = heappop(current)
            ans.append(temp[1])
            
        return ans
                
        
        
        
        
        