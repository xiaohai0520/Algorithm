class Solution:

    def __init__(self, w: List[int]):
        self.sum = sum(w)
        self.len = len(w)
        for i in range(1, len(w)):
            w[i] += w[i - 1]
        self.cum_sum = w
        

    def pickIndex(self):
        """
        :rtype: int
        """
        
        num = random.randint(1, self.sum)
        
        low, high = 0, self.len - 1
        while low < high:
            mid = low + (high - low)//2
            if self.cum_sum[mid] < num:
                low = mid + 1
            else:
                high = mid
        return low
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
