This is a greedy problem.

We want to split as many parts as possible.

So we only need to save the last index of each each.

iterate the S and each time we find the largest end.

If the index == end. we think no more char should be included



Code:
    
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = {}
        for i,c in enumerate(S):
            dic[c] = i
        res = []
        
        start = end = 0
        for i,c in enumerate(S):
            end = max(end,dic[c])
            if i == end:
                res.append(end-start+1)
                start = end + 1
        return res
