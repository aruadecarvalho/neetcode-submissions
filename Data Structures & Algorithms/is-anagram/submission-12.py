class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_count = defaultdict(int)
        for char in s:
            s_char_count[char] +=1 
        

        t_char_count = defaultdict(int)
        for char in t:
            t_char_count[char] +=1 

        return t_char_count == s_char_count