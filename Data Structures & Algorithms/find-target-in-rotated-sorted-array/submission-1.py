class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif nums[low] == target:
                return low
            elif nums[high] == target:
                return high
            elif nums[low] < nums[high]:
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] < nums[mid]:
                    if nums[mid] < target:
                        low = mid + 1
                    else:
                        if nums[low] < target:
                            high = mid - 1
                        else:
                            low = mid + 1
                else:
                    if nums[mid] < target:
                        if nums[low] < target:
                            high = mid - 1
                        else:
                            low = mid + 1
                    else:
                        high = mid - 1

        return -1