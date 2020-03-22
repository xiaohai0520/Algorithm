class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            
            cur = set()
            for i in range(1,int(num**0.5) + 1):
                if num % i == 0:
                    cur.add(i)
                    cur.add(num//i)
                if len(cur) > 4:
                    break
            if len(cur) == 4:
                res += sum(cur)
        return res
