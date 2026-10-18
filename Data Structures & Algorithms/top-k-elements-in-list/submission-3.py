class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {} 
        buckets = [[] for i in range(len(nums) + 1)]

        for i in nums:
            frequency[i] = 1 + frequency.get(i, 0)

        for num, count in frequency.items():
            buckets[count].append(num)

        topk = []
        for i in range(len(nums), 0, -1):
            for j in buckets[i]:
                topk.append(j)
                if len(topk) == k:
                    return topk
        return topk