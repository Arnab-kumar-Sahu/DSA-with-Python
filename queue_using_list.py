class Queue:
    def __init__(self):
        self.start=[]
    def is_empty(self):
        return self.start==[]
    def enqueue(self,data):
        self.start.append(data)
    def dequeue(self):
        if not self.is_empty():
            return self.start.pop(0)
        else:
            raise IndexError
    def get_front(self):
        if not self.is_empty():
            return self.start[0]
        else:
            raise IndexError
    def get_rear(self):
        if not self.is_empty():
            return self.start[-1]
        else:
            raise IndexError
    def size(self):
        return len(self.start)
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.get_front())
print(q.get_rear())
q.dequeue()
print(q.get_front())
print(q.get_rear())



