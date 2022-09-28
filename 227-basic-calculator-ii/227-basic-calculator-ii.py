class Solution:
    def calculate(self, s: str) -> int:
        s += "+0"
        pre = "+"
        stack, num = [], 0
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif not s[i].isspace():
                if pre == "/":
                    temp = int(stack.pop()/num)
                    stack.append(temp)
                elif pre == "*":
                    temp = stack.pop()*num
                    stack.append(temp)
                elif pre == "-":
                    stack.append(-num)
                else:
                    stack.append(num)
                pre, num = s[i], 0
            
        return sum(stack)