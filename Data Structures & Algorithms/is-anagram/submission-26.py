class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = defaultdict(int) # O(n)
        for c in s:
            s_count[c] += 1

        for c in t:
            if s_count[c]:
                s_count[c] -= 1
            
            if s_count[c] == 0:
                del s_count[c]

        return len(s_count.keys()) == 0
                

