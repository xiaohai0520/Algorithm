class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k != 0:
            return False
        nums.sort()
        dic = collections.Counter(nums)
        for num in nums:
            count = dic[num]
            if count == 0:
                continue
            for i in range(k):
                if dic[num + i] < count:
                    return False
                dic[num + i] -= count
        return True
        
