class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ht = {}
        for l in s:
            if l in s_ht:
                s_ht[l] += 1
            else:
                s_ht[l] = 1
        
        print(s_ht)

        for l in t:
            if l not in s_ht:
                return False
            
            s_ht[l] -= 1
            if s_ht[l] == 0:
                del s_ht[l]
        
        return s_ht == {}
        