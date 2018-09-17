
#we can also use set to instead of node

class Node:
    
    def __init__(self,x):
        self.val = x
        self.mini = None


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mystack = []
        self.mins = float('inf')
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        node = Node(x)
        
        node.mini = min(self.mins,x)
        
        self.mins = min(self.mins,x)
        
        self.mystack.append(node)
        

    def pop(self):
        """
        :rtype: void
        """
        cur = self.mystack.pop()
        curmin = cur.mini
        if curmin == self.mins:
            if self.mystack:
                self.mins = self.mystack[-1].mini
            else:
                self.mins = float('inf')

            
        return cur.val
        
        
        

    def top(self):
        """
        :rtype: int
        """
        
        return self.mystack[-1].val
        
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
