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
        for s in freq_s1:
            if freq_s1[s] == freq_s2[s]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == need:
                return True
            
            outgoing = s2[l]
            freq_s2[outgoing] -= 1
            if outgoing in freq_s1 and freq_s2[outgoing] == freq_s1[outgoing]:
                matches += 1
            elif outgoing in freq_s1 and freq_s2[outgoing] + 1 == freq_s1[outgoing]:
                matches -= 1
            
            incoming = s2[r]
            freq_s2[incoming] += 1
            if incoming in freq_s1 and freq_s2[incoming] == freq_s1[incoming]:
                matches += 1
            elif incoming in freq_s1 and freq_s2[incoming] - 1 == freq_s1[incoming]:
                matches -= 1
            
            l += 1

        return matches == need

