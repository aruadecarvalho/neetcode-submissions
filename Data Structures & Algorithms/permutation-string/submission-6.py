class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = [0] * 26
        for s in s1:
            s1_freq[ord(s) - ord("a")] += 1
       
        curr_freq = [0] * 26
        l = 0
        for r in range(len(s2)):
            index = ord(s2[r]) - ord("a")
            curr_freq[index] += 1

            while curr_freq[index] > s1_freq[index]:
                curr_freq[ord(s2[l]) - ord("a")] -= 1
                l += 1
            
            if r - l + 1 == len(s1):
                return True
        
        return False
