class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        count = 0
        startIndex = 0
        arr = [i for i in range(1, n+1)]
        while count != n - 1:
            count += 1
            temp = 0
            while temp != k:
                if arr[startIndex] != 0:
                    temp += 1
                if temp != k:
                    startIndex = (startIndex + 1) % n
            arr[startIndex] = 0
            
            while arr[startIndex] == 0:
                startIndex = (startIndex + 1) % n
                
        for num in arr:
            if num != 0:
                return num