class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list = []
        for x in range(1,n+1):
            if x%5==0 and x%3==0:
                list.append("FizzBuzz")
            elif x%3==0:
                list.append("Fizz")
            elif x%5==0:
                list.append("Buzz")
            else:
                list.append(str(x))
        return list
