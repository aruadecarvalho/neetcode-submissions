class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        freq_t = defaultdict(int)
        for c in t:
            freq_t[c] += 1
        
        freq_s = defaultdict(int)
        have, need = 0, len(freq_t)
        l = 0
        best_len = float('inf')
        best_start = 0
        for r in range(len(s)):
            if s[r] in freq_t:
                freq_s[s[r]] += 1
                if freq_s[s[r]] == freq_t[s[r]]:
                    have += 1

            while have == need:
                match_len = r - l + 1
                if match_len < best_len:
                    best_start = l
                    best_len = match_len

                if s[l] in freq_t:
                    freq_s[s[l]] -= 1
                    if freq_s[s[l]] < freq_t[s[l]]:
                        have -= 1

                l += 1

        if best_len == float('inf'):
            return ""
        
        return s[best_start:best_start + best_len]