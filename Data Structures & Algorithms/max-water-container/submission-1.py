class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bottom = 0
        top = len(heights) - 1
        area = 0
        while bottom < top:
            newArea = min(heights[bottom], heights[top]) * (top - bottom)
            area = max(area, newArea)
            if heights[bottom] < heights[top]:
                bottom += 1
            else:
                top -= 1
        return area