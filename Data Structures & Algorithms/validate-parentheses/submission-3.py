class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {'}':'{', ']':'[', ')':'('}
        for char in s:
            if char == '{' or char == '[' or char == '(':
                stack.append(char)
            else:
                if len(stack) == 0 or stack.pop() != matching[char]:
                    return False
        return len(stack) == 0