class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] # (h, i)
        res = 0
        for i, h in enumerate(height):
            while stack and h > stack[-1][0]:
                stack_h, stack_i = stack.pop()
                if not stack:
                    break
                bounded_height = min(h, stack[-1][0]) - stack_h
                distance = i - stack[-1][1] - 1
                res += bounded_height * distance

            stack.append((h, i))
        
        return res