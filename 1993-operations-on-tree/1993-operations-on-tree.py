class LockingTree:

    def __init__(self, parent: List[int]):
        self.graph = defaultdict(list)
        for i in range(1, len(parent)):
            self.graph[parent[i]].append(i)
        
        self.condition = [[0, 0] ] * len(parent)
        self.ancestor = defaultdict(list)
        
        def dfs(node, path):
            self.ancestor[node] = path.copy()
            for child in self.graph[node]:
                path.append(node)
                dfs(child, path)
                path.pop()
        dfs(0, []) 
        
        self.decendant = defaultdict(list)
        def dp(node):
            
            for child in self.graph[node]:
                val = dp(child)
                for v in val:
                    self.decendant[node].append(v)
                    
            temp = self.decendant[node].copy()
            temp.append(node)
            return temp.copy()
        dp(0)
        
        # print(self.decendant)
        # print(self.ancestor)

    def lock(self, num: int, user: int) -> bool:
        if self.condition[num][0] == 1:
            return False
        self.condition[num] = [1, user]
        return True
    
    def unlock(self, num: int, user: int) -> bool:
        if self.condition[num][0] == 0:
            return False
        elif self.condition[num][1] != user:
            return False
        self.condition[num] = [0, 0]
        return True
    
    def upgrade(self, num: int, user: int) -> bool:
        if self.condition[num][0] == 1:
            return False
        
        def check_descendant(num):
            for child in self.decendant[num]:
                if self.condition[child][0] == 1:
                    return True
            return False
        
        def check_ancestor(num):
            for child in self.ancestor[num]:
                if self.condition[child][0] == 1:
                    return False
            return True
        
        flag = check_descendant(num) and check_ancestor(num)
        
        if flag:
            self.condition[num] = [1, user]
            for child in self.decendant[num]:
                self.condition[child] = [0, 0]
            return True
        
        return False


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)

# 0 = unlocked
# 1 = locked
# 2 = upgrade