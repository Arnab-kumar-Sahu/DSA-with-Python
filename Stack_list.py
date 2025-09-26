class Stack(list):
    def is_empty(self):
        return self==[]
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("out of index")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("ou of index")
    def size(self):
        return len(self)
    def insert(self):
        raise AttributeError("no Attribute named insert")
    def extend(self):
        raise AttributeError("no Attribute named extend")

    def remove(self):
        raise AttributeError("no Attribute named append")


a=Stack()
a.push(4)
print(a.peek())
a.insert()