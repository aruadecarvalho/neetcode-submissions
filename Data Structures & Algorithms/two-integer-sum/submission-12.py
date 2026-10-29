class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3, 4, 5, 6], since the array is not sorted we cant
        # use two pointers and iterate over it from 0 to i until they find a pair
        # we know that nums[i] + nums[j] == target
        # we know that there is only one pair that satisfies this problem
        # we can store a number and its compliment to see if we find the match
        # {target - [nums[i]]: i}
        # if we get the nums[j], then we know nums[i] exists, and we can return that pair

        seen = {}
        for i in range(len(nums)):
            if seen.get(nums[i]) != None:
                return [seen[nums[i]], i]
            
            seen[target - nums[i]] = i
        
        return [0,0]