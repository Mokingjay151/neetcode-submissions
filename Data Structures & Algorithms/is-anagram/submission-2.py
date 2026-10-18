class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = list(s)
        t_letters = list(t)
        s_letters.sort()
        t_letters.sort()
        return s_letters == t_letters

        