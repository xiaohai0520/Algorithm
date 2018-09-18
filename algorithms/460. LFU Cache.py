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
