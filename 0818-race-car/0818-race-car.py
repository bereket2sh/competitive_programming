class Solution:
    def racecar(self, target: int) -> int:
        visited = {(0, 1): True}
        queue = [[0,1, 0]] # pos, speed, ins
        
        def traverse(pos, speed, ins):
            nonlocal queue, visited, target
            if 0 <= pos < 2*target and (pos, speed) not in visited:
                queue.append([pos, speed, ins+1])
                visited[(pos, speed)] = True
                
        while queue:
            pos, speed, ins = queue.pop(0)
            if pos == target:
                return ins
            traverse(pos + speed,  2*speed, ins)
            traverse(pos,  -1 if speed > 0 else 1, ins)