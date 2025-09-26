class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Queue:
    def __init__(self,start=None):
        self.start=start
        self.size=0
    def is_empty(self):
        return self.start is None
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.start=n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        self.size+=1
    def dequeue(self):
        if not self.is_empty():
            self.size-=1
            res=self.start
            self.start=self.start.next
            return res.item
        else:
            raise IndexError
    def get_front(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError
    def get_rear(self):
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            return temp.item
        else:
            raise IndexError
    def size(self):
        return self.size

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.get_front())
print(q.get_rear())
q.dequeue()
print(q.get_front())
print(q.get_rear())

