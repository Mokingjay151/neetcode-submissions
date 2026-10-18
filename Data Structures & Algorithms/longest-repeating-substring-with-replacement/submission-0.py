class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = list(s)
        alpha = set(s)
        longest = 0
        for c in alpha:
            l = 0
            count = 0
            for r in range(0, len(arr)):
                if arr[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if arr[l] == c:
                        count -= 1
                    l += 1
                longest = max(longest, r - l + 1)
        return longest