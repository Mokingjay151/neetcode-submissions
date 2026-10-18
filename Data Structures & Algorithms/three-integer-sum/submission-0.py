class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet = []
        tripletList = []
        nums.sort()
        a = 1
        b = len(nums) - 1

        for i in range(0, len(nums)):
            a = i + 1
            b = len(nums) - 1
            while a < b:
                if nums[a] + nums[b] > -nums[i]:
                    b -= 1
                elif nums[a] + nums[b] < -nums[i]:
                    a += 1
                else:
                    triplet = [nums[i], nums[a], nums[b]]
                    triplet.sort()
                    a += 1
                if triplet not in tripletList and len(triplet) > 0:
                    tripletList.append(triplet)
        return tripletList