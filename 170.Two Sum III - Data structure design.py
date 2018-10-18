#use the dic to save the number and ues diff in dict to find the another one
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.dict[number] = self.dict.get(number,0) + 1
            
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.dict:
            if (value - num) in self.dict and (value - num != num or self.dict[num] > 1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
