class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        curr = 0
        for n in nums:
            if n == 1:
                curr += 1
                if curr >= max:
                    max = curr
            else:
                curr = 0
        
        return max