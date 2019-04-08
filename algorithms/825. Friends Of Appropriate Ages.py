class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        res = 0
        count = [0]*121
        for i in ages:
            count[i]+=1
        s = [0]*121
        for i in range(1,121):
            s[i] = s[i-1]+count[i]
        for i in range(15,121):
            if count[i]!=0:
                num = s[i]-s[int(math.floor(i*0.5+7))]
                res += num*count[i]-count[i]
        return res
            
