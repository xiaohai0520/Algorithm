class Solution:
    def isNumber(self, s: str) -> bool:
        if len(s) == 0:
            return False
        dot, digit = 0, 0 
        i = 0 
        s = s.strip() + " "  # space, placeholder
        if s[i] =="+" or s[i] == "-":
            i += 1 
        while s[i].isdigit() or s[i] == ".":
            if s[i] == ".":
                dot += 1
            if s[i].isdigit():
                digit += 1
            i += 1 
        if dot > 1 or digit <= 0:
            return False
        if s[i] == "e":
            if s[i+1] == "+" or s[i+1] == "-":
                i += 1 
            sright = s[i+1:]
            if not sright.strip().isdigit():
                return False
            i += len(sright)
        return len(s)-1 == i
