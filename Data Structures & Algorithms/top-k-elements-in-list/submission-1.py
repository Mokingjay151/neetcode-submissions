class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        occur = {}
        topk = []
        for i in nums:
            if i not in occur:
                occur[i] = 1
            else:
                occur[i] = occur[i] + 1
        for i in range(0, k):
            max = 0
            maxOccur = 0
            for j in occur.keys():
                if occur[j] > maxOccur:
                    maxOccur = occur[j]
                    max = j
            topk.append(max)
            occur.pop(max)
        return topk