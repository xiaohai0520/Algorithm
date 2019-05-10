class Solution:
    def countAndSay(self, n: int) -> str:
        word="1"
        ans=""
        if n==1:
            return word
        for times in range(n-1):
            count=0
            for index in range(len(word)):
                if(index==0):
                    say=word[index]
                    count=1
                elif(say==word[index]):
                    count+=1
                else:
                    ans=ans+str(count)+str(say)
                    say=word[index]
                    count=1

            ans=ans+str(count)+str(say)
            word=ans
            ans=""
        return word
