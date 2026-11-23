class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        freq_s1 = defaultdict(int)
        freq_s2 = defaultdict(int)
        for i in range(len(s1)):
            freq_s1[s1[i]] += 1
            freq_s2[s2[i]] += 1
        
        matches = 0
        need = len(freq_s1)
        for k in freq_s1:
            if freq_s2[k] == freq_s1[k]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == need:
                return True
        
            freq_s2[s2[l]] -= 1
            if s2[l] in freq_s1 and freq_s2[s2[l]] == freq_s1[s2[l]]:
                matches += 1
            elif s2[l] in freq_s1 and freq_s2[s2[l]] == freq_s1[s2[l]] - 1:
                matches -= 1
    
            freq_s2[s2[r]] += 1
            if s2[r] in freq_s1 and freq_s2[s2[r]] == freq_s1[s2[r]]:
                matches += 1
            elif s2[r] in freq_s1 and freq_s2[s2[r]] == freq_s1[s2[r]] + 1:
                matches -= 1
            
            l += 1
            
        return matches == need