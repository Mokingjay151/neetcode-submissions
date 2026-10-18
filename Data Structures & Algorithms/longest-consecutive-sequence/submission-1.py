class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: # Return 0 for empty list
            return 0
        nums.sort()
        longest = 0
        current = 1
        for i in range(0, len(nums)):
            if i + 1 < len(nums): # If there is a next element
                if nums[i + 1] == nums[i] + 1: # If consecutive then increment counter
                    current += 1
                elif nums[i + 1] > nums[i] + 1:
                    current = 1
            if current >= longest: # Update longest consecutive count
                longest = current
        return longest