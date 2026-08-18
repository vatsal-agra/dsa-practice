class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 2):    
            w = s[i:i+3]                
            if len(set(w)) == 3:        
                count += 1
        return count