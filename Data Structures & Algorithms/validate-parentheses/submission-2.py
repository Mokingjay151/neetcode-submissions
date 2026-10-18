class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {'}':'{', ']':'[', ')':'('}
        top = -1
        for char in s:
            if char in ['{', '[', '(']:
                stack.append(char)
                top += 1
            else:
                if top < 0 or stack.pop(top) != matching[char]:
                    return False
                top -= 1
        return len(stack) == 0