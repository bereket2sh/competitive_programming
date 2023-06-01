class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = [i for i in range(n)]
        
        def find(node):
            while node != parent[node]:
                node = parent[node]
            return node
        
        def union(a, b, m):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            parent[pb] = pa
            
            for c, d in restrictions:
                if find(c) == find(d):
                    ans[m] = False
                    parent[pb] = pb
                    break
            
        
            
        ans = [True]*len(requests)

        for i in range(len(requests)):
            a, b = requests[i][0], requests[i][1]
            union(a, b, i)
            
        return ans