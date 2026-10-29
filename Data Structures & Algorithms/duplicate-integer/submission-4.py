class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup = dict()
        for i in nums:
            if  i not in lookup:
                lookup[i] = 1
            else:
                lookup[i] += 1
            if lookup[i] > 1:
                return True
        return False