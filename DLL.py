class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class DLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_first(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n
    def insert_at_end(self,data):
        if self.is_empty():
            n=Node(None,data,None)
            self.start=n
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            n=Node(temp,data,None)
            temp.next=n
    def insert_after(self,target,data):
        temp=self.start
        while temp!=None and temp.item!=target:
            temp=temp.next
        if temp:
            n=Node(temp,data,temp.next)
            if temp.next:
                temp.next.prev=n
            temp.next=n
    def insert_many(self,*data):
        for i in data:
            self.insert_at_end(i)
    def insert_range(self,data):
        for i in data:
            self.insert_at_end(i)
    def search(self,data):
        temp=self.start
        while temp!=None:
            if temp.item==data:
                return True
            temp=temp.next
        return False
    def print_list(self):
        temp=self.start
        while temp!=None:
            print(temp.item,end='->')
            temp=temp.next
        print()
    def delete_first(self):
        if self.is_empty():
            pass
        elif self.start.next==None:
            self.start=None
        else:
            self.start=self.start.next
            self.start.prev=None
    def delete_end(self):
        if self.is_empty():
            pass
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            if temp.prev:
                temp.prev.next=None
            else:
                self.start=None
    def delete_value(self,data):
        if self.is_empty():
            pass
        else:
            temp=self.start
            while temp!=None:
                if temp.item==data:
                    if temp.next!=None:
                        temp.next.prev=temp.prev
                    if temp.prev!=None:
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.next
                    break
                temp=temp.next
    def delete_all(self):
        self.start=None
    def __iter__(self):
        return DLLIterator(self.start)
class DLLIterator:
    def __init__(self,start):
        self.temp=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.temp!=None:
            res=self.temp.item
            self.temp=self.temp.next
            return res
        raise StopIteration
L=DLL()
L.insert_at_first(456)
L.insert_many(1,2,3,34,4,5,54,5,343,2,32,3)
L.print_list()
L.delete_first()
L.print_list()
L.delete_all()
L.print_list()
L.insert_range(range(1,100))
L.print_list()