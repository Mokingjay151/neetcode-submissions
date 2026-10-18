class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        bottom = 0
        top = len(numbers) - 1
        while bottom <= top:
            if numbers[bottom] + numbers[top] < target:
                bottom += 1
            elif numbers[bottom] + numbers[top] > target:
                top -= 1
            else:
                return [bottom + 1, top + 1]
        return []
