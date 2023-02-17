class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A):
            
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
                
                # print("".join(A))
            
            else:
                A.append("(")
                generate(A)
                A.pop()
                A.append(")")
                generate(A)
                A.pop()
                
        def valid(S):
            var = 0
            for c in S:
                if c == "(":
                    var += 1
                else:
                    var -= 1
                if var < 0:
                    return False
            return var == 0
            
        ans = []
        generate([])
        return ans
                    