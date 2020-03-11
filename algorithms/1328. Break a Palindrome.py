class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        p = palindrome
        if len(p) == 1:  # corner case
            return ""
        p = list(p)  # convert to list in order to modify
        for i, ch in enumerate(p):
            if ch != 'a' and i != len(p) // 2:  # e.g: "aba"
                p[i] = 'a'  # modify
                break
            if i == len(p) - 1:  # the last element
                p[i] = 'b'  # e.g: "aaa"
        return "".join(p)
