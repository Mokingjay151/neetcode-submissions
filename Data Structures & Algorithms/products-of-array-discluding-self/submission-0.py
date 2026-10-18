class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        product = 1
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j:
                    product = product * nums[j]
            products.append(product)
            product = 1
        return products