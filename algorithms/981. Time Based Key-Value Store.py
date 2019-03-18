class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.vals[key].append([timestamp,value])
    
    def search(self,key,timestamp):
        arr = self.vals[key]
        l,r = 0,len(arr)-1
        cur = ''
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] > timestamp:
                r = mid - 1
            else:
                cur = arr[mid][1]
                l = mid + 1
        return cur
    
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key in self.vals:
            return self.search(key,timestamp)
        return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
