# use dictionary and circle linklist 
# each node has last and next 
# add node to root next and the last is always the LRU

class node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.last = None


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.root = node(None,None)
        self.root.next = self.root
        self.root.last = self.root
        self.dic = {}
        self.cap = capacity
        
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        root,dic = self.root, self.dic
        if key not in dic:
            return -1
        cur = dic[key]
        cur.last.next = cur.next
        cur.next.last = cur.last
        
        # root.next.last,cur.next,root.next,cur.last = cur,root.next,cur,root
        
        root.next.last = cur
        cur.next = root.next
        root.next = cur
        cur.last = root
        
        return dic[key].value
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
    
        cap,root,dic = self.cap, self.root, self.dic
        if cap == 0:
            return
        
        if key in dic:
            dic[key].value = value
            self.get(key)
            return
        l = len(dic)
        if l >= cap:
            evict = root.last
            evict.last.next = root
            root.last = evict.last
            del dic[evict.key]
        cur = node(key,value)
        cur.next = root.next
        cur.last = root
        root.next.last = root.next = cur
        
        dic[key] = cur
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
