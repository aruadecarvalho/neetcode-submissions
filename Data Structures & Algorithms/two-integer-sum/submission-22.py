class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[i] + nums[j] = target
        # compliment (nums[j]) = target - current nums[i]

        seen = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in seen:
                return [seen[nums[i]], i]
            
            seen[target - nums[i]] = i
        
        return [0, 0]