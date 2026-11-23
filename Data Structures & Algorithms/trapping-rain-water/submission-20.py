class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                mid_i = stack.pop()
                if len(stack) == 0:
                    continue
                left_i = stack[-1]
                w = i - left_i - 1
                h = min(height[left_i], height[i]) - height[mid_i]
                res += w * h
            
            stack.append(i)
        
        return res
            