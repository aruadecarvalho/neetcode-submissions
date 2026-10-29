class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i, n in enumerate(nums):
            arr.append([n, i])
        
        arr.sort()

        l, r = 0, len(nums) - 1
        while l < r:
            print(l, r)
            if arr[l][0] + arr[r][0] == target:
                return [
                    min(arr[l][1], arr[r][1]),
                    max(arr[l][1], arr[r][1])
                ]
            
            if target - arr[r][0] < arr[l][0]:
                r -= 1
                continue
            
            l += 1