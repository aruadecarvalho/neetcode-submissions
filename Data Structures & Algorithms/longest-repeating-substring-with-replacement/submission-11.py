class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(s)):
            char_freq[s[r]] += 1

            while (r - l + 1) - max(char_freq.values()) > k:
                char_freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res
