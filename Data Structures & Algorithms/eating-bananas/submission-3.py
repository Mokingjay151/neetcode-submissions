import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        n = len(piles) - 1
        min = piles[n]
        low = 1
        high = piles[n]
        while low <= high:
            total = 0
            mid = (high + low) // 2
            for i in piles:
                total += math.ceil(i / mid)
            if total <= h:
                high = mid - 1
                if mid < min:
                    min = mid
            else:
                low = mid + 1

        return min