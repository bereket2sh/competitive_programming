class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # indegree = [0]*numCourses
        graph = collections.defaultdict(list)
        hasCycle = False
        visited = set()
        deadends = set()
        
        for l,r in prerequisites:
            graph[r].append(l)
        # print(graph)
            
        def dfs(node):
            nonlocal hasCycle
            if node in deadends:
                return
            # print(node)
            # print(node)
            visited.add(node)
            
            for n in graph[node]:
                # print(n)
               
                if n in visited:
                    hasCycle = True
                    continue
                if n not in deadends:
                    # print(n)
                    dfs(n)
            ans.append(node)
            # print(ans)
            visited.remove(node)
            deadends.add(node)

        ans = []
        
        for r in range(numCourses):
            dfs(r)
            
        # print(ans)
        if len(ans) >= numCourses and not hasCycle:
            ans.reverse()
            return ans
        return []