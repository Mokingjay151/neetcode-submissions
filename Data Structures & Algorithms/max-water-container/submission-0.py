class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        b = len(heights) - 1
        volume = min(heights[a], heights[b]) * (b - a)
        if len(heights) == 2:
            return volume
        
        while b > a:
            if heights[a] < heights[b]:
                a += 1
            else:
                b -= 1
            newVolume = min(heights[a], heights[b]) * (b - a)
            if newVolume > volume:
                volume = newVolume
        return volume