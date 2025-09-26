class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next
class PriorityQueue:
    def __init__(self,start=None):
        self.start=start
        self.item_count=0
    def is_empty(self):
        return self.start is None
    def push(self,data,p):
        n=Node(data,p)
        if self.is_empty():
            self.start=n
        else:
            if self.start.priority>=p:
                n.next=self.start
                self.start=n
                self.item_count+=1
                return
            temp=self.start
            while temp.next!=None and temp.next.priority<p:
                temp=temp.next
            if temp:
                n.next=temp.next
                temp.next=n
        self.item_count+=1
    def pop(self):
        if self.is_empty():
            raise IndexError
        res=self.start
        self.start=self.start.next
        self.item_count-=1
        return res.item
    def size(self):
        return self.item_count
p=PriorityQueue()
p.push(10,0)
p.push(20,-1)
p.push(30,1)
print(p.pop())
print(p.size())




