class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        courses.sort(key = lambda x : x[1])
        
        heap = []
        current_time = 0
        
        
        for duration, lastday in courses:
            if current_time + duration > lastday:
                if heap and -heap[0] > duration:
                    current_time += heappop(heap) + duration
                    heappush(heap, -duration)
                    
            else:
                heappush(heap, -duration)
                current_time += duration
                
        return len(heap)
                    
            