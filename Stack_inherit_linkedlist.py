from SLL import *
class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count=0
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_first(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            res=self.start
            self.delete_first()
            self.item_count-=1
            return res.item
        else:
            raise IndexError
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError
    def size(self):
        return self.item_count
s=Stack()
s.push(10)
s.push(40)
s.push(30)
print(s.peek())
s.pop()
print(s.peek())


