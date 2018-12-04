class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.max:
            self.max.append(x)
        else:
            self.max.append(max(x,self.max[-1]))

    def pop(self):
        """
        :rtype: int
        """
        self.max.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.max[-1]

    def popMax(self):
        """
        :rtype: int
        """
        m = self.max[-1]
        cur = []
        while m != self.stack[-1]:
            cur.append(self.stack.pop())
            self.max.pop()
        self.stack.pop()
        self.max.pop()
        while cur:
            self.push(cur.pop())
        return m
        
        
        

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
