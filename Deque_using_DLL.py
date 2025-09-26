class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class Deque:
    def __init__(self,front=None,rear=None):
        self.front=front
        self.rear=rear
        self.item_count=0
    def is_empty(self):
        return self.item_count==0
    def insert_front(self,data):
        n=Node(item=data)
        if self.is_empty():
            self.front=n
            self.rear=n
        else:
            n.next=self.front
            self.front.prev=n
            self.front=n
        self.item_count+=1
    def insert_rear(self,data):
        n=Node(item=data)
        if self.is_empty():
            self.front=n
            self.rear=n
        else:
            n.prev=self.rear
            self.rear.next=n
            self.rear=n
        self.item_count+=1
    def delete_front(self):
        if  self.is_empty():
            raise IndexError
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front.next.prev=None
            self.front=self.front.next
        self.item_count-=1
    def delete_rear(self):
        if  self.is_empty():
            raise IndexError
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.rear.prev.next=None
            self.rear=self.rear.prev
        self.item_count-=1
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise Exception("empty queue")
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise Exception("empty queue")
    def size(self):
        return self.item_count
q=Deque()
q.insert_rear(10)
q.insert_front(20)
q.insert_front(30)
print(q.get_front())
print(q.get_rear())
q.delete_rear()
print(q.get_rear())
print(q.size())