class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        result = []
        def helper(pos, cur, count):
            if len(word) == pos:
                # Once we reach the end, append current to the result
                result.append(cur + str(count) if count > 0 else cur)
            else:
                # Skip current position, and increment count
                helper(pos + 1, cur, count + 1)
                # Include current position, and zero-out count
                helper(pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0)

        
        helper(0, '', 0)
        return result 
