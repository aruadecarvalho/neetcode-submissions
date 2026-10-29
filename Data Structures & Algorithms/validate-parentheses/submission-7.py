class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []

        for l in s:
            if l in open_to_close.keys():
                stack.append(l)
            else:
                if len(stack) == 0:
                    return False
                                    
                last = stack.pop()
                if l != open_to_close[last]:
                    return False
        
        return len(stack) == 0

        