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
        if not self.stack:
            self.stack.append(x)
            self.max.append(x)
        else:
            self.stack.append(x)
            if x > self.max[-1]:
                self.max.append(x)
            else:
                self.max.append(self.max[-1])
        
        

    def pop(self):
        """
        :rtype: int
        """
        if self.stack:
            self.max.pop()
            return self.stack.pop()
        
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        

    def peekMax(self):
        """
        :rtype: int
        """
        if self.max:
            return self.max[-1]

    def popMax(self):
        """
        :rtype: int
        """
        cur = []    
        maxv = self.max[-1]
        while self.stack:
            if maxv != self.stack[-1]:
                cur.append(self.stack.pop())
                self.max.pop()
            else:
                self.max.pop()
                self.stack.pop()
                break
        
        while cur:
            self.push(cur.pop())
            
        return maxv
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
