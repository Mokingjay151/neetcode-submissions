class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        map = {i:[i] for i in nums}
        starts = []
        for i in map:
            if i - 1 not in map:
                starts.append(i)
        for i in starts:
            j = 1
            while i + j in map:
                map[i].append(i + j)
                j += 1
            if len(map[i]) > longest:
                longest = len(map[i])
        return longest