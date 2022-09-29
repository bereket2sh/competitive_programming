class Solution:
    def decodeString(self, s: str) -> str:
        stack, curString, num = [], "", 0
        
        for c in s:
            
            if c == "[":
                stack.append(curString)
                stack.append(num)
                num = 0
                curString = ""
                
            elif c.isdigit():
                num = num*10 + int(c)
                
            elif c == "]":
                num = stack.pop()
                prevString = stack.pop()
                
                curString = prevString + curString * num
                num = 0
                
            else:
                curString += c
                
        return curString