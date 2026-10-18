class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        final = [0] * n
        for i in range(n):
            if not stack or temperatures[i] <= stack[-1][0]:
                stack.append((temperatures[i], i))
            else:
                while stack and temperatures[i] > stack[-1][0]:
                    temp, index = stack.pop()
                    final[index] = i - index
                stack.append((temperatures[i], i))
        return final