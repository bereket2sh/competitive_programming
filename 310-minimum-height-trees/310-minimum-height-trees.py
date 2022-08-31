class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 2:
            return[0]
        graph = defaultdict(list)
        outdegree = [0]*n
        
        for s,e in edges:
            graph[s].append(e)
            graph[e].append(s)
            
            outdegree[s] += 1
            outdegree[e] += 1
        
        que = []
        for i in range(len(outdegree)):
            if outdegree[i] == 1:
                que.append(i)
                
        remaining = n
        while remaining > 2:
            remaining -= len(que)
            newQue = []
            
            while que:
                node = que.pop()
                

                for parent in graph[node]:
                    outdegree[parent] -= 1
                    if outdegree[parent] == 1:
                       
                        
                        newQue.append(parent)
                        
            
            que = newQue
                    
        return que
                
        