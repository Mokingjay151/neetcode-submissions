class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = "".join(strs) # Concatenate all strings together
        encoded = str(len(encoded)) + "~" + encoded # Add total length of all strings to the front with a delimiter ~
        lengths = [] # Lengths of each individual string
        for i in strs:
            lengths.append(len(i)) # Record length of each string
        encoded = encoded + str(lengths) # Concatenate list of lengths of each string to the end
        return encoded

    def decode(self, s: str) -> List[str]:
        tilda = s.index("~") # Index of delimiter ~
        total_length = int(s[0 : tilda]) # Total length of all strings
        strings = s[tilda + 1 : tilda + total_length + 1] # Concatenated strings
        lengths = s[tilda + total_length + 1 :] # List of lengths of each string
        lengths = lengths[1:-1] # Remove brackets
        lengths = lengths.replace(" ", "") # Remove whitespaces
        lengths = lengths.split(",") # Convert to list
        if lengths[0] == '':
            return []

        decoded = [] # List of strings
        index = 0
        for i in lengths:
            decoded.append(strings[index : index + int(i)])
            index += int(i)
        return decoded