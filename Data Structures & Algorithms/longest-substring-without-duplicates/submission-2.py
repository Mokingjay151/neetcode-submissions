class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        arr = list(s)
        left = 0
        window = 0
        longest = 0
        for r in range(0, len(arr)):
            if arr[r] not in letters:
                letters[arr[r]] = r
                window += 1
            else:
                left = max(left, letters[arr[r]] + 1)
                letters[arr[r]] = r
                longest = max(longest, window)
                window = r - left + 1
        longest = max(longest, window)
        return longest