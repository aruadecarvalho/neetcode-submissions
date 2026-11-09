class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_asc = curr = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                curr = 0
            
            curr += nums[i]
            max_asc = max(curr, max_asc)
        
        return max_asc