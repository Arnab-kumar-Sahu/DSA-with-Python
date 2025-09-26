class Node:
    def __init__(self,item=None,prev=None):
        self.item=item
        self.prev=prev
class Stack:
    def __init__(self):
        self.top=None
        self.count=0
    def is_empty(self):
        return self.top==None
    def push(self,data):
        n=Node(data)
        n.prev=self.top
        self.top=n
        self.count+=1
    def pop(self):
        if not self.is_empty():
            self.count -= 1
            temp=self.top
            self.top=self.top.prev
            return temp.item

    def peek(self):
        if not self.is_empty():
            return self.top.item
    def size(self):
        return self.count
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.peek())
print(s.pop())
print(s.size())
print(s.pop())
print(s.pop())
print(s.is_empty())