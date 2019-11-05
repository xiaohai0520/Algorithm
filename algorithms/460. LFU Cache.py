
# OrderedDict in python is implemented by a dict+linkedList, which is essentially a LRU cache.
# "keyfreq" dict represents a normal dict that maps one key to one frequency.
# "freqkeys" dict represents a dict that maps one freq to many keys, and these "many keys" are stored in OrderedDict.
# With this two dicts, given one key, we can find its frequency, and with its frequency, we can find all other keys of the same frequency.
# When there are many items of same frequency, the OrderedDict in freqkeys dict correctly records the item order in LRC fashion where the first item will be the one to pop out.

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.minfreq=None
        self.keyfreq={}
        self.freqkeys=collections.defaultdict(collections.OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.keyfreq:
            return -1
        freq=self.keyfreq[key]
        val=self.freqkeys[freq][key]
        del self.freqkeys[freq][key]
        if not self.freqkeys[freq]:
            if freq==self.minfreq:
                self.minfreq+=1
            del self.freqkeys[freq]
        self.keyfreq[key]=freq+1
        self.freqkeys[freq+1][key]=val
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity<=0:
            return
        if key in self.keyfreq:
            freq=self.keyfreq[key]
            self.freqkeys[freq][key]=value
            self.get(key)
            return
        if self.capacity==len(self.keyfreq):
            delkey,delval=self.freqkeys[self.minfreq].popitem(last=False)
            del self.keyfreq[delkey]
        self.keyfreq[key]=1
        self.freqkeys[1][key]=value
        self.minfreq=1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



#want to say nothing

LAST, NEXT, KEY, VAL, FREQ = 0, 1, 2, 3, 4 
class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {} #key -> [LAST, NEXT, KEY, VAL, FREQ]
        self.freq_dic = {} #freq -> root: [LAST, NEXT, None, None, FREQ]
        self.least_freq = 1
        self.cap = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        dic, freq_dic, cap = self.dic, self.freq_dic, self.cap
        if key not in dic:
            return -1
        node = dic[key]
        node[NEXT][LAST], node[LAST][NEXT] = node[LAST], node[NEXT]
        freq = node[FREQ]
        if freq == self.least_freq and freq_dic[freq][NEXT] is freq_dic[freq]:
            self.least_freq += 1
        
        node[FREQ] += 1
        freq = node[FREQ]
        if freq not in freq_dic:
            root = []
            root[:] = [root, root, None, None, freq]
            freq_dic[freq] = root
        root = freq_dic[freq]
        root[LAST][NEXT], root[LAST], node[NEXT], node[LAST] = node, node, root, root[LAST]
        return node[VAL]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        dic, freq_dic, cap = self.dic, self.freq_dic, self.cap
        if cap == 0:
            return
        if key in dic:
            self.get(key)
            dic[key][VAL] = value
            return
        
        if cap == len(dic):
            evict = freq_dic[self.least_freq][NEXT]
            evict[NEXT][LAST], evict[LAST][NEXT] = evict[LAST], evict[NEXT]
            del dic[evict[KEY]]
        self.least_freq = 1
        if 1 not in self.freq_dic:
            root = []
            root[:] = [root, root, None, None, 1] 
            freq_dic[1] = root
        
        root = freq_dic[1]
        node = [None, None, key, value, 1]
        root[LAST][NEXT], root[LAST], node[NEXT], node[LAST] = node, node, root, root[LAST]
        dic[key] = node
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
