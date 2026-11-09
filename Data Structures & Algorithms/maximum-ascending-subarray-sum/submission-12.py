class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_asc = 0
        curr = nums[0]

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                curr += nums[i]

            max_asc = max(curr, max_asc)

            if nums[i - 1] >= nums[i]:
                curr = nums[i]
        
        return max_asc