# use a array and a dic(remember the position)


import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ls = []
        self.dic = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        
        self.dic[val] = len(self.ls)
        self.ls.append(val)
        return True
        
        
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        index = self.dic[val]
        last = self.ls[-1]
        
        self.ls[index] = last
        self.dic[last] = index
        self.ls.pop()
        del self.dic[val]
        return True
            
        
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.ls)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
