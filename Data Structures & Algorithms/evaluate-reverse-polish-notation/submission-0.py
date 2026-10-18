class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = int(tokens[0])
        stack = []
        for i in tokens:
            if i == '+':
                ans = stack.pop() + stack.pop()
                stack.append(ans)
            elif i == '-':
                ans = - stack.pop() + stack.pop()
                stack.append(ans)
            elif i =='*':
                ans = stack.pop() * stack.pop()
                stack.append(ans)
            elif i =='/':
                divisor = stack.pop()
                ans = int(stack.pop() / divisor)
                stack.append(ans)
            else:
                stack.append(int(i))
        return ans