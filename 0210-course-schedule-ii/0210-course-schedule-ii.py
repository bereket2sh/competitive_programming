class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        hasCycle = False
        visited = set()
        deadends = set()
        
        for l,r in prerequisites:
            graph[r].append(l)
            
        def dfs(node):
            nonlocal hasCycle
            if node in deadends:
                return
            
            visited.add(node)
            
            for n in graph[node]:
               
                if n in visited:
                    hasCycle = True
                    continue
                if n not in deadends:
                    dfs(n)
                    
            ans.append(node)
            visited.remove(node)
            deadends.add(node)

        ans = []
        
        for r in range(numCourses):
            dfs(r)
            
        if len(ans) >= numCourses and not hasCycle:
            ans.reverse()
            return ans
        return []