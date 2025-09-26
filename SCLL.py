class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class SCLL:
    def __init__(self,last=None):
        self.last=last
    def is_empty(self):
        return self.last==None
    def insert_at_first(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    def insert_after(self,target,data):
        if self.is_empty():
            return
        n=Node(data)
        temp=self.last.next
        while True:
            if temp.item==target:
                n.next=temp.next
                temp.next=n
                if temp==self.last:
                    self.last=n
                return
            temp=temp.next
            if temp==self.last.next:
                print("target is not present")
                return
    def insert_many(self,*data):
        for i in data:
            self.insert_at_last(i)

    def print_list(self):
        if self.is_empty():
            return
        temp=self.last.next
        while True:
            print(temp.item,end='->')
            temp=temp.next
            if temp==self.last.next:
                break
        print()
    def search(self,data):
        if self.is_empty():
            return
        temp=self.last.next
        while True:
            if temp.item==data:
                return True
            temp=temp.next
            if temp==self.last.next:
                return False
    def delete_first(self):
        if self.is_empty():
            return
        elif self.last==self.last.next:
            self.last=None
            return
        else:
            self.last.next=self.last.next.next
    def delete_end(self):
        if self.is_empty():
            return
        if self.last==self.last.next:
            self.last=None
            return
        temp=self.last.next
        while temp.next!=self.last:
            temp=temp.next
        temp.next=self.last.next
        self.last=temp
    def delete_value(self,data):
        if self.is_empty():
            return
        if self.last.next.item==data:
            if self.last.next==self.last:
                self.last=None
                return
            else:
                self.last.next=self.last.next.next
        temp = self.last.next
        while temp.next != self.last.next:
            if temp.next.item == data:
                if temp.next == self.last:
                    self.last = temp
                temp.next = temp.next.next
                return
            temp = temp.next
    def __iter__(self):
        if self.is_empty():
            return SCLLIterator(None)
        return SCLLIterator(self.last.next)
class SCLLIterator:
    def __init__(self,start):
        self.start=start
        self.curr=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.curr==None:
            raise StopIteration
        if self.curr==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        res=self.curr
        self.curr=self.next
        return res

L=SCLL()
L.insert_many(1,2,3,4,5,6,7,8,9)
L.print_list()
L.insert_at_first(456)
L.print_list()
L.insert_at_last(222)
L.print_list()
L.delete_value(4)
L.print_list()



