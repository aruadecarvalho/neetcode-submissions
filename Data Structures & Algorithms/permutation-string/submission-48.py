class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        freq_s1 = defaultdict(int)
        freq_s2 = defaultdict(int)

        for i in range(len(s1)):
            freq_s1[s1[i]] += 1
            freq_s2[s2[i]] += 1
        
        match = 0
        need = len(freq_s1)

        for c in freq_s1:
            if freq_s1[c] == freq_s2[c]:
                match += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if match == need:
                return True
        
            outgoing = s2[l]
            freq_s2[outgoing] -= 1
            if outgoing in freq_s1:
                if freq_s2[outgoing] == freq_s1[outgoing]:
                    match += 1
                elif freq_s2[outgoing] + 1 == freq_s1[outgoing]:
                    match -= 1
            
            incoming = s2[r]
            freq_s2[incoming] += 1
            if incoming in freq_s1:
                if freq_s2[incoming] == freq_s1[incoming]:
                    match += 1
                elif freq_s2[incoming] - 1 == freq_s1[incoming]:
                    match -= 1

            l += 1

        return match == need
