from collections import OrderedDict
class LRUCache:
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        if key in self.cache: del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)



class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        
        self.cache = dict()
        self.keyList = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        if(key in self.cache):
            
            if key in self.keyList:
                self.keyList.remove(key)
                self.keyList.append(key)
            
            else:
                self.keyList.append(key)
                
            return self.cache[key]
        
        
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #Check if cache length is less than = capacity
        if key not in self.cache:
            if(len(self.cache) < self.capacity):
            
                self.cache.update({key: value})
                
                if key in self.keyList:
                    self.keyList.remove(key)
                    self.keyList.append(key)
            
                else:
                    self.keyList.append(key)
        
            else:
                #Pop LRU key
                keyToPop = self.keyList[0]
                self.keyList.remove(keyToPop)
                self.cache.pop(keyToPop)
            
                self.cache.update({key: value})
                
                if key in self.keyList:
                    self.keyList.remove(key)
                    self.keyList.append(key)
            
                else:
                    self.keyList.append(key)
        
        else:
            self.cache.update({key: value})
            
            if key in self.keyList:
                self.keyList.remove(key)
                self.keyList.append(key)
            
            else:
                self.keyList.append(key)