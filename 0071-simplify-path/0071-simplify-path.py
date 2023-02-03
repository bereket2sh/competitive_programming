class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        p = 0
        while p < len(path):
            temp = ""
            
            while p < len(path) and path[p] != "/":
                temp += path[p]
                p += 1
            if temp:
                stack.append(temp)
            p += 1
            
        for i in range(len(stack)):
            if stack[i] == ".":
                stack[i] = "n/a"
            elif stack[i] == "..":
                j = i - 1
                while j >= 0:
                    if stack[j] != "n/a":
                        stack[j] = "n/a"
                        break
                    j -= 1
                    
                stack[i] = "n/a"
                
        ans = ""
        print(stack)
        for s in stack:
            if s != "n/a":
                ans += "/" + s
                
        return ans if ans else "/"
                
        
        