This problem we can see the subarray.

We the subarray we need to think about the dict

divide by K means remainder is 0

we need to remember the previous remainder number 

if we meet the same remainder, add that number is OK.


CODE:
    
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        dic = collections.defaultdict(int)
        dic[0] = 1
        res = 0
        pre = 0
        for a in A:
            pre += a
            re = pre%K
            res += dic[re]
            dic[re] += 1
        return res
