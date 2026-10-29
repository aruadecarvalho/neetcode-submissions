class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i, n in enumerate(nums):
            arr.append([n, i])
        
        arr.sort()

        l, r = 0, len(nums) - 1
        while l < r:
            cur = arr[l][0] + arr[r][0]
            if cur == target:
                return [
                    min(arr[l][1], arr[r][1]),
                    max(arr[l][1], arr[r][1])
                ]
            
            if cur < target:
                l += 1
            else:
                r -= 1
        
        return []