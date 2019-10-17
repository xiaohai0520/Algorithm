# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    
    def __init__(self, iterator):

    
        self.it = iterator
        if iterator.hasNext()==True:
            self.Current = iterator.next()
        else:
            self.Current=None


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.Current


    def next(self):
        """
        :rtype: int
        """
        temp = self.Current
        if self.it.hasNext()==True:
            self.Current=self.it.next()
        else:
            self.Current=None
        return temp


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.Current==None:
            return False
        return True
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
