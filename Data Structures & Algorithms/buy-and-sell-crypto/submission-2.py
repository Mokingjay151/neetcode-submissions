class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        high = 1
        net = 0
        for i in range(1, len(prices)):
            if prices[low] > prices[i]:
                net = max(net, prices[high] - prices[low])
                low = i
                high = i
            elif prices[high] <= prices[i]:
                high = i
                net = max(net, prices[high] - prices[low])
        return net