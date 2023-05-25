class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = [i for i in range(n)]
        answer = [False] * len(requests)
        rank = [1 for _ in range(n)]
        
        def find1(node):
            while node != parent[node]:
                node = parent[node]
                
            return parent[node]
        
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
                
            return parent[node]
        
        def union(a, b, i):
            pa = find(a)
            pb = find(b)
            
            if pa != pb:
                parent[pb] = pa
                flag = True
                
                for x, y in restrictions:
                    px, py = find1(x), find1(y)
                    if px == py:
                        flag = False
                        break
                        
                if flag:
                    answer[i] = True
                else:
                    
                    parent[pb] = pb 
                
                
            else:
                answer[i] = True
                
        for i in range(len(requests)):
            union(requests[i][0], requests[i][1], i)
        
        return answer
            
            