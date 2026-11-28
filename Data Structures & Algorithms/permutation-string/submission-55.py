class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq_s1 = [0] * 26
        freq_s2 = [0] * 26

        for i in range(len(s1)):
            freq_s1[ord(s1[i]) - ord('a')] += 1
            freq_s2[ord(s2[i]) - ord('a')] += 1
        
        match = sum(1 for i in range(26) if freq_s1[i] == freq_s2[i])
        
        l = 0
        for r in range(len(s1), len(s2)):
            if match == 26:
                return True
        
            outgoing = ord(s2[l]) - ord('a')
            freq_s2[outgoing] -= 1
            if freq_s2[outgoing] == freq_s1[outgoing]:
                match += 1
            elif freq_s2[outgoing] + 1 == freq_s1[outgoing]:
                match -= 1
            
            incoming = ord(s2[r]) - ord('a')
            freq_s2[incoming] += 1
            if freq_s2[incoming] == freq_s1[incoming]:
                match += 1
            elif freq_s2[incoming] - 1 == freq_s1[incoming]:
                match -= 1

            l += 1

        return match == 26
