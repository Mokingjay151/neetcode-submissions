class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        map = defaultdict(list)
        for s in strs:
            frequency = [0] * 26
            for char in s:
                frequency[ord(char) - 97] += 1
            map[tuple(frequency)].append(s)
        return list(map.values())