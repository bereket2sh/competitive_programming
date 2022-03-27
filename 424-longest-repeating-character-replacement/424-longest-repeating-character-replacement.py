class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #space, time = O(n*k),O(26)--->O(1)
        Dict = {}
        left = 0
        res = 0
        
        for right in range(len(s)):
            Dict[s[right]] = 1 + Dict.get(s[right],0) #Dict.get(s[rght],0) this will return 0 if s[right]is  not in the dictionoary
            while right-left+1 - max(Dict.values()) > k: #max(Dict.values()) has time complexity  O(26)
                Dict[s[left]] -= 1
                left += 1
                
            res = max(res,right-left+1)  #right - left + 1 is the size of the window
            
        return res