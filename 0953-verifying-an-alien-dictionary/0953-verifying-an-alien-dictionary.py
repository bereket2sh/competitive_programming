class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = defaultdict(int)
        for i, char in enumerate(order):
            dic[char] = i
        
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                fst, sec = words[i][0], words[j][0]
                
                if  fst != sec:
                    if dic[fst] > dic[sec]:
                        return False
                    
                else:
                    flag = True
                    k = 1
                    while k < len(words[i]) and k < len(words[j]):
                        if words[i][k] != words[j][k]:
                            flag = False
                            if dic[words[i][k]] > dic[words[j][k]]:
                                # print(here)
                                return False
                            break
                        k += 1
                            
                    if flag:
                        if len(words[i]) > len(words[j]):
                            return False
                        
        return True
                    
                
                