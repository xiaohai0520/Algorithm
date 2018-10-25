class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        string = ''
        for s in strs:
            string += str(len(s))
            string += ' '
            string += s
        return string

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        if s == '':
            return []
        
        ans = []
        start = 0
        size = len(s)
        length = 0
        while start < size:
            if s[start] != ' ':
                length *= 10
                length += int(s[start])
                start += 1
            elif s[start] == ' ':
                start += 1
                ans.append(s[start:start+length])
                start += length
                length = 0

        return ans

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
