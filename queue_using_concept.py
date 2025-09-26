class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.item_count==0
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
            self.rear = n
        else:
            self.rear.next=n
            self.rear = n
        self.item_count+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("empty queue")
        elif self.front==self.rear:
            self.rear=None
            self.front=None
        else:
            self.front=self.front.next
        self.item_count-=1
    def get_front(self):
        if self.is_empty():
            raise IndexError("empty queue")
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("empty queue")
        else:
            return self.rear.item
    def size(self):
        return self.item_count
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.get_front())
print(q.get_rear())
q.dequeue()
print(q.get_front())
print(q.get_rear())