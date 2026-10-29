class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_char_count = defaultdict(int)
        for char in s:
            s_char_count[char] +=1 
        
        for char in t:
            if char not in s_char_count:
                return False
            else: 
                s_char_count[char] -= 1
                
            if s_char_count[char] == 0:
                del s_char_count[char]
        
        return s_char_count == {}