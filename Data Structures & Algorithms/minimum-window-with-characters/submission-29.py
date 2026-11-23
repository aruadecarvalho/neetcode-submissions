class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        freq_s = defaultdict(int)
        freq_t = defaultdict(int)
        for c in t:
            freq_t[c] += 1
        
        have, need = 0, len(freq_t)
        best_start, best_len = 0, len(s) + 1
        l = 0
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
        if best_len == len(s) + 1:
            return ""

        return s[best_start:best_start + best_len]