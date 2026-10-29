class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash_table = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in nums_hash_table:
                diff_i = nums_hash_table.get(difference)
                return [min(i, diff_i), max(i, diff_i)]
            
            nums_hash_table[nums[i]] = i