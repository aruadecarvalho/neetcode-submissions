class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] # (h, i)
        res = 0
        for i, h in enumerate(height):
            while stack and h > stack[-1][0]:
                mid, _ = stack.pop()
                if not stack:
                    break
                right = h
                left = stack[-1][0]
                water = min(right, left) - mid
                w = i - stack[-1][1] - 1
                res += water * w

            stack.append((h, i))
        
        return res