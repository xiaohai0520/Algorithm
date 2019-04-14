This is a match problem.

It means that the pattern can add any char to match the query

So we need to think that the query need to have the same Captical of the pattern and the lowercase can not include the query not have.

We iterite the query and if we find the match char in both word, the index of pattern plus 1.

if the query inclue a upper case which pattern not the next right capitcal, it also return False.


Example 1:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation: 
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".


Code:

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        
        def helper(q):
            index = 0
            for ch in q:
                if index < len(pattern) and ch == pattern[index]:
                    index += 1
                    continue
                if ch.isupper():
                    return False
            return index == len(pattern)
        
        for q in queries:
            res.append(helper(q))
        return res
