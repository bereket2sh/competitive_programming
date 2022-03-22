class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prev = points[0][1]
        arrows = 1
        for i in range(1,len(points)):
            if points[i][0] > prev:
                arrows += 1
                prev = points[i][1]
            else:
                prev = min(prev,points[i][1])
        return arrows
#         points.sort(key=lambda x:x[1])
#         print(points)
#         arrow = 1
#         end = points[0][1]
#         for i in range (1,len(points)):
#             if points[i][0] > end:
#                 arrow += 1
#                 end = points[i][1]
            
#         return arrow