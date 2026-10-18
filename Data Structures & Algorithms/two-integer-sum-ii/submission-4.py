class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Nested loop to match each element of the list with every other element
        for i in range(0, len(numbers)):
            if i == 0 or numbers[i] != numbers[i - 1]:
                for j in range(i, len(numbers)):
                    if numbers[i] + numbers[j] == target and i < j: # Check if the sum is the desired total and that i < j
                        return [i + 1, j + 1]
