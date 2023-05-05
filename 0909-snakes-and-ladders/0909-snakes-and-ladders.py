class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        val = [[0 for i in range(n)] for i in range(n)]
        temp = 1
        toggle = 1
        
        for i in range(n-1, -1, -1):
            if toggle:
                for j in range(0, n):
                    val[i][j] = temp
                    temp += 1
            else:
                for j in range(n-1, -1, -1):
                    val[i][j] = temp
                    temp += 1
            
            toggle = 1 - toggle
      
            
        coordinates = defaultdict(list)
        for i in range(n):
            for j in range(n):
                coordinates[val[i][j]] = [i, j]

        queue = deque([(1, 1)])
        depth = 0
        visited = set([1])
        
        while queue:
            print(queue)
            new_queue = deque()
            
            while queue:
                # print("true")
                # print(queue)
                cur_val, ladder = queue.popleft()

                if cur_val == n**2:
                    return depth
                r, c = coordinates[cur_val][0], coordinates[cur_val][1]

                for i in range(cur_val + 1, min(n**2 + 1, cur_val +  7)):
                    
                    # print(i, coordinates[i])
                    row, col = coordinates[i][0], coordinates[i][1]

                    if board[row][col] != -1 and board[row][col] not in visited :
                        if i == 15:
                            print(i, ladder)
                        # if ladder:
                        visited.add(board[row][col])
                        new_queue.append((board[row][col], 0))


                        # elif i not in visited:
                            
                            # visited.add(i)
                            # new_queue.append((i, 1))

                    elif board[row][col] == -1 and i not in visited:
                        # print(i)
                        visited.add(i)
                        new_queue.append((i, 1))
                        
           
            queue = new_queue
            
            depth += 1
                    
                    
        return -1
        
# [-1, 42, 12, -1, 1, -1, -1]
# [-1, -1, 5, -1, -1, 46, 44]
# [18, 22, 6, 39, -1, -1, -1]
# [-1, -1, 40, -1, -1, -1, 37]
# [49, 38, 24, -1, 14, 29, -1]
# [-1, -1, 6, -1, -1, -1, 20]
# [-1, -1, 12, 10, -1, 5, 26]

# [43, 44, 45, 46, 47, 48, 49]
# [42, 41, 40, 39, 38, 37, 36]
# [29, 30, 31, 32, 33, 34, 35]
# [28, 27, 26, 25, 24, 23, 22]
# [15, 16, 17, 18, 19, 20, 21]
# [14, 13, 12, 11, 10, 9, 8]
# [1, 2, 3, 4, 5, 6, 7]

               
                