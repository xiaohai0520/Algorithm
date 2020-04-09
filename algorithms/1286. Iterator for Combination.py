class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.n = combinationLength
        self.st = characters
        self.ls = []
        self.helper('',0)
        self.index = 0
        #print(self.ls)
    def helper(self,path,start):

        if len(path) == self.n:
            self.ls.append(path)
            return
        for i in range(start,len(self.st)):
            self.helper(path+self.st[i],i+1)
        

        
    def next(self) -> str:
        cur = self.ls[self.index]
        self.index += 1
        return cur
        

    def hasNext(self) -> bool:
        
        if self.index < len(self.ls):
            return True
        return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
