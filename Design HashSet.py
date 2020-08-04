class MyHashSet:

    def __init__(self):
        self.arr=[False]*1000001

    def add(self, key):
        self.arr[key]=True

    def remove(self, key):
        self.arr[key]=False

    def contains(self, key):
        if self.arr[key]:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
