class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        minimum = 1000
        if nums[low] < nums[high]:
            return nums[low]
        while low < high:
            mid = (high + low) // 2
            if nums[low] < nums[high]:
                return min(minimum, nums[low])
            elif nums[low] > nums[high] and nums[mid] > nums[low]:
                low = mid + 1
            elif nums[low] > nums[high] and nums[mid] < nums[high]:
                high = mid - 1
            else:
                return min(minimum, nums[high])
            if nums[mid] < minimum:
                minimum = nums[mid]
        return min(minimum, nums[low])