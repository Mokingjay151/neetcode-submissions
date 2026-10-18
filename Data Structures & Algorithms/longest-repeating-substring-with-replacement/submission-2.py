class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxFrequency = 0
        l = 0
        longest = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxFrequency = max(maxFrequency, count[s[r]])

            while (r - l + 1) - maxFrequency > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest