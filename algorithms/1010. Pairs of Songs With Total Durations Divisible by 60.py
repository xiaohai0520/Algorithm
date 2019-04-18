This is a array and math problem.

It is as same as the two sum problem.

every time we search the other part of the remainder, and save the remainder.

The problem is to find the 0 condition.

code:
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if not time:
            return 0
        dic = collections.defaultdict(int)
        res = 0
        for t in time:
            res += dic[(60 - t % 60)%60]
            dic[t%60] += 1
        return res
