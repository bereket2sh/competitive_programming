class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        count = {}
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
            count[recipes[i]] = len(ingredients[i])
            
        queue = deque(supplies)
        res = []
        
        while queue:
            temp = queue.popleft()
           
            if temp in graph:
                for recipe in graph[temp]:
                    count[recipe] -= 1
                    if count[recipe] == 0:
                        queue.append(recipe)
                        res.append(recipe)
                        
        return res
                        