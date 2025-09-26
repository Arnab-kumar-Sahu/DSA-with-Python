from SLL import *
class Stack:
    def __init__(self):
        self.top=SLL()
        self.item_count=0
    def is_empty(self):
        return self.top.is_empty()
    def push(self,data):
      self.top.insert_at_first(data)
      self.item_count+=1
    def pop(self):
        if not self.is_empty():
            self.item_count-=1
            res=self.top.start.item
            self.top.delete_first()
            return res
        else:
            raise IndexError
    def peek(self):
        if not self.is_empty():
            return self.top.start.item
        else:
            raise IndexError
    def size(self):
        return self.item_count
s=Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())
s.pop()
print(s.peek())