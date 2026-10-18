class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() # Convert string to all lower case
        bottom = 0
        top = len(s)
        while bottom <= top:
            while not s[bottom:bottom + 1].isalnum():
                bottom += 1
                if bottom > top:
                    return True
            while not s[top - 1:top].isalnum():
                top -= 1
                if top < bottom:
                    return True
            if s[bottom:bottom + 1] != s[top - 1:top]:
                return False
            bottom += 1
            top -= 1
        return True