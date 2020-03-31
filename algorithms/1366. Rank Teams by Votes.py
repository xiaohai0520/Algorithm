class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 1:
            return votes[0]
        l = len(votes[0])
        dic = collections.defaultdict(lambda:[0]*l)
        
        for each in votes:
            for i,ch in enumerate(each):
                dic[ch][i] += 1
        ls = list(votes[0])
        ls.sort(key=lambda x:[-i for i in dic[x]] + [x])
        return ''.join(ls)
    
    
    

            
