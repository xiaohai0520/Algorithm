# use dictionary and circle linklist 
# each node has last and next 
# add node to root next and the last is always the LRU

class node:
    
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = node(None,None)
        self.head.next = self.head
        self.head.pre = self.head
        self.dic = {}
        self.cap = capacity
        
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        cur = self.dic[key]
        val = cur.val
        
        cur.pre.next,cur.next.pre = cur.next,cur.pre
        
        cur.next = self.head.next
        cur.pre = self.head
        self.head.next = cur
        cur.next.pre = cur
        

        return val


    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            
            self.dic[key].val = value
            self.get(key)
            return
        new = node(key,value)
        
        
        new.next = self.head.next
        new.pre = self.head
        self.head.next = new
        new.next.pre = new
        
        self.dic[key] = new
        
        if len(self.dic) > self.cap:
            cur = self.head.pre
            self.head.pre,cur.pre.next = cur.pre,self.head
            del self.dic[cur.key]
            
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
