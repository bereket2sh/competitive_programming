class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        graph_row = defaultdict(list)
        indegree_row = [0] * k
        graph_col = defaultdict(list)
        indegree_col = [0] * k
        
        position = defaultdict(list)
        ans = []
        for i in range(k):
            temp = []
            for i in range(k):
                temp.append(0)
            ans.append(temp)
        
        for a, b in rowConditions:
            graph_row[a].append(b)
            indegree_row[b - 1] += 1
            
        for a, b in colConditions:
            graph_col[a].append(b)
            indegree_col[b - 1] += 1
            
            
        def topological(g, ind):
            
            que = deque()
            
            for i, val in enumerate(ind):
                if val == 0:
                    que.append(i + 1)
                    
            order = []
            
            while que:
                temp = que.popleft()
                order.append(temp)
                
                for child in g[temp]:
                    ind[child - 1] -= 1
                    if ind[child - 1] == 0:
                        que.append(child)
                        
            return order
                        
        row = topological(graph_row, indegree_row)
        col = topological(graph_col, indegree_col)
        
        if len(row) < k or len(col) < k:
            return []
        
        for r, x in enumerate(row):
            c = col.index(x)
            ans[r][c] = x
            
        return ans
            