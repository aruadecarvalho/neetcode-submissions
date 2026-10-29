class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = defaultdict(int)
        for c in s: # O(n)
            s_count[c] += 1

        for c in t: # O(m)
            if s_count[c]:
                s_count[c] -= 1
            
            if s_count[c] == 0:
                del s_count[c]

        return len(s_count.keys()) == 0
                

