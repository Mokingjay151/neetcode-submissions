class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        bottom = 0
        longest = 0
        for top in range(len(s)):
            if s[top] in letters:
                bottom = max(bottom, letters[s[top]] + 1)
            letters[s[top]] = top
            longest = max(longest, top - bottom + 1)
        return longest