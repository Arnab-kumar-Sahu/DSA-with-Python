class Priority_queue:
    def __init__(self):
        self.start=[]
    def is_empty(self):
        return self.start==[]
    def push(self,data,priority):
        self.start.insert(priority,data)
    def pop(self):
        if self.is_empty():
            raise IndexError
        return self.start.pop(0)
    def size(self):
        return len(self.start)
p=Priority_queue()
p.push(5,0)
p.push(12,100)
p.push(45,(-20))
print(p.size())
print(p.pop())


