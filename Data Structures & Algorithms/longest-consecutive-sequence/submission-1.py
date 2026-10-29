class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [0, 3, 2, 5, 4, 6, 1, 1]
        nums_set = set(nums)
        longest = 0
        for n in nums_set:
            if (n - 1) not in nums_set:
                length = 1
                while (n + length) in nums_set:
                    length += 1
                
                longest = max(longest, length)
        
        return longest