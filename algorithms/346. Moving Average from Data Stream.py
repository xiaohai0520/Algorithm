#if we use queue,after size ,just pop left and append right


class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.ls = []
        self.size = size
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        # dic[val] = len(ls)
        self.ls.append(val)
        if len(self.ls) < self.size:      
            return sum(self.ls) / len(self.ls)
        
        return sum(self.ls[len(self.ls)-self.size:])/self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
