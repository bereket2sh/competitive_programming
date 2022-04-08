class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            
        indegree = [0]*numCourses
        for i in graph:
            for j in graph[i]:
                indegree[j] += 1
        
        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        courseOrder = []
        while queue:
            pre = queue.popleft()
            courseOrder.append(pre)
            for course in graph[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
                    
        if len(courseOrder) == numCourses:
            return courseOrder
        else: return []