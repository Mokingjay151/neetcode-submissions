class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() # Convert string to all lower case
        forward = []
        for i in s: # Go through each character
            if i.isalnum(): # If it is an alphanumeric character, add it to the list
                forward.append(i)
        s = s[::-1] # Reverse string and repeat process
        backward = []
        for i in s:
            if i.isalnum():
                backward.append(i)
        return forward == backward