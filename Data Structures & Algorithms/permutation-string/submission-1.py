class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        frequency1 = [0] * 26
        frequency2 = [0] * 26
        for char in s1:
            frequency1[ord(char) - 97] += 1
        for i in range(len(s1)):
            frequency2[ord(s2[i]) - 97] += 1
        if frequency1 == frequency2:
            return True
        for i in range(len(s1), len(s2)):
            frequency2[ord(s2[i]) - 97] += 1
            frequency2[ord(s2[i - len(s1)]) - 97] -= 1
            if frequency1 == frequency2:
                return True
        return False