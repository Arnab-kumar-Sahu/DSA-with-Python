class Node:
    def __init__(self, left=None, item=None, right=None):
        self.left = left
        self.item = item
        self.right = right


class Bst:
    def __init__(self, root=None):
        self.root = root

    def insert_node(self, data):
        n = Node(item=data)
        temp = self.root
        if self.root == None:
            self.root = n
            return
        while True:
            if temp.item == data:
                return "duplicate node"
            if temp.item < data:
                if temp.right == None:
                    temp.right = n
                    return
                temp = temp.right
            elif temp.item > data:
                if temp.left == None:
                    temp.left = n
                    return
                temp = temp.left
    def recursion_insert(self,data):
        def insert(root,data):
            if root==None:
                return Node(item=data)
            if root.item<data:
                root.right=insert(root.right,data)
            elif root.item>data:
                root.left=insert(root.left,data)
            return root
        self.root=insert(self.root,data)

    def search(self,data):
        temp=self.root
        while True:
            if temp==None:
                return
            if temp.item==data:
                return temp
            if temp.item<data:
                temp=temp.right
            elif temp.item>data:
                temp=temp.left
    def recursion_search(self,data):
        def find(root,data):
            if root==None:
                return False
            if root.item==data:
                return True
            if root.item<data:
                return find(root.right,data)
            else:
                return find(root.left,data)
        return find(self.root,data)

    def traverse(self):
        def t(x):
            if x == None:
                return
            t(x.left)
            print(x.item)
            t(x.right)
        t(self.root)
    def min_value(self):
        temp=self.root
        while temp.left !=None:
            temp=temp.left
        return temp.item
    def max_value(self):
        temp=self.root
        while temp.right!=None:
            temp=temp.right
        return temp.item
    def re_min_value(self):
        def get(temp):
            if temp==None:
                return"node is empty"
            if temp.left==None:
                return temp.item
            return get(temp.left)
        return get(self.root)
    def re_max_value(self):
        def get(temp):
            if temp==None:
                return "node ia empty"
            if temp.right==None:
                return temp.item
            return get(temp.right)
        return get(self.root)
    def delete_node(self):

b = Bst()
b.insert_node(50)
b.insert_node(60)
b.insert_node(70)
b.insert_node(10)
b.insert_node(20)
b.traverse()
r=b.search(10)
print(r.item)
min=b.re_min_value()
print(min)
