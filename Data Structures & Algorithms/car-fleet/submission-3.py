class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = list(zip(position, speed))
        pos_speed.sort(reverse=True)
        stack = []
        ans = 0
        for i in pos_speed:
            time = (target - i[0]) / i[1]
            if not stack or time > stack[-1]:
                stack.append(time)
                ans += 1
        return ans