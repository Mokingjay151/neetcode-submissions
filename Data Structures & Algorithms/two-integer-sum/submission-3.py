class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        i = 0
        j = 1
        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]].append(i)
            else:
                map[nums[i]] = [i]
        for k in map:
            if target - k in map:
                i = map[k][0]
                if len(map[target - k]) > 1:
                    j = map[target - k][1]
                else:
                    j = map[target - k][0]
                if i < j:
                    break
        return [i, j]