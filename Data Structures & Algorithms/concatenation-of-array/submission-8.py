class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        new_array = [0] * (size * 2)

        for i in range(0, size):
            new_array[i] = nums[i]
            new_array[size + i] = nums[i]
            
        return new_array
        