class CustomStack:
    def __init__(self, maxSize):
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x):
        if len(self.inc) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        if not self.inc: return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k, val):
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val
    
    
    
    
#     def __init__(self, maxSize: int):
#         self.cap = maxSize
#         self.stack = []

#     def push(self, x: int) -> None:
#         if len(self.stack) >= self.cap:
#             return
#         self.stack.append(x)
        
        

#     def pop(self) -> int:
#         if not self.stack:
#             return -1
#         return self.stack.pop()

#     def increment(self, k: int, val: int) -> None:
#         for i in range(len(self.stack)):
#             if i < k:
#                 self.stack[i] += val
                
        
        
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
