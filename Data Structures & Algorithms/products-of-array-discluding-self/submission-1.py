class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1, nums[0]]
        products = []
        for i in range(2, len(nums)):
            prefix.append(prefix[i - 1] * nums[i - 1])

        suffix = [1, nums[len(nums) - 1]]
        for i in range(2, len(nums)):
            suffix.append(suffix[i - 1] * nums[-i])

        for i in range(0, len(nums)):
            products.append(prefix[i] * suffix[-1 - i])
        return products