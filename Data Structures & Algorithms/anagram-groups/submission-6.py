class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = list(s)
        s_letters.sort()
        t_letters = list(t)
        t_letters.sort()
        return s_letters == t_letters


    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groupedAnagrams = []
        top = len(strs)
        while top > 0:
            anagramSet = []
            while top > 0:
                if self.isAnagram(strs[0], strs[top - 1]):
                    anagramSet.append(strs[top - 1])
                    del strs[top - 1]
                top -= 1
            top = len(strs)
            groupedAnagrams.append(anagramSet)
        return groupedAnagrams