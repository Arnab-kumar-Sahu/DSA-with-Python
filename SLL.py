class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_first(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_end(self,data):
        n=Node(data)
        if self.is_empty():
            self.start=n
        else:
            temp=self.start
            while temp.next != None:
                temp=temp.next
            temp.next=n
    def insert_after(self,target,data):
        temp=self.start
        while temp!=None and temp.item!=target:
            temp=temp.next
        if temp:
            n=Node(data,temp.next)
            temp.next=n
    def insert_many(self,*data):
        for i in data:
            self.insert_at_end(i)
    def insert_list(self,data):
        for i in data:
            self.insert_at_end(i)
    def search(self,target):
        temp=self.start
        while temp!=None:
            if temp.item==target:
                return True
            temp=temp.next
        else:
            return False
    def print_list(self):
        temp=self.start
        while temp !=None:
            print(temp.item,end='->')
            temp=temp.next
        print()
    def delete_first(self):
        if self.is_empty():
            pass
        else:
            self.start=self.start.next
    def delete_end(self):
        if self.is_empty():
            pass
        elif self.start.next==None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
    def delete_value(self,data):
        if self.is_empty():
            pass
        elif self.start.item==data:
            self.start=self.start.next
        else:
            temp=self.start
            while  temp.next!=None and temp.next.item!=data :
                temp=temp.next
            if temp.next:
                temp.next=temp.next.next
    def __iter__(self):
        return Sll_iterator(self.start)
class Sll_iterator:
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



if __name__=='__main__':
    LL = SLL()
    LL.insert_many(1,2,3,4,5,6,7,8,9)
    LL.delete_value(7)
    LL.delete_first()
    LL.insert_after(3, 33)
    LL.insert_list([100, 200])
    LL.print_list()

    for i in LL:
        print(i, end='->')
    print()


