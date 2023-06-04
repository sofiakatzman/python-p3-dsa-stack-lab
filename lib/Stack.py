class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit


    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else: 
            return False 

    def push(self, item):
        if (not self.full()):
            self.items.append(item)
        else: 
            return 

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if (len(self.items) >= self.limit):
            return True
        else: 
            return False

    def search(self, target):
        for i in range(len(self.items)):
            if self.items[i] == target:
                return len(self.items) -1  - i 
        return -1
    
    def empty(self):
        self.items= []
