class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        remove_duplicates = set(nums)
        nums2 = list(remove_duplicates)
        return len(nums2) != len(nums)