class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list) # content as a key and the path as value
       
        for path in paths:
            
            path, *files = path.split()
            for file in files:
                file, content = file.split("(")
                hashMap[content[:-1]].append(path + "/" + file)
                
        res = []
        for key in hashMap:
            if len(hashMap[key]) > 1:
                res.append(hashMap[key])

        return res