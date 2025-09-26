class Deque:
    def __init__(self):
        self.start=[]
    def is_empty(self):
        return self.start==[]
    def insert_front(self,data):
        self.start.insert(0,data)
    def insert_rear(self,data):
        self.start.append(data)
    def delete_first(self):
        if not self.is_empty():
            self.start.pop(0)
    def delete_rear(self):
        if not self.is_empty():
            self.start.pop(-1)
    def get_front(self):
        return self.start[0]
    def get_rear(self):
        return self.start[-1]
    def size(self):
        return len(self.start)
q=Deque()
q.insert_rear(10)
q.insert_front(20)
q.insert_front(30)
print(q.get_front())
print(q.get_rear())
q.delete_rear()
print(q.get_rear())
print(q.size())