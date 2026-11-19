class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Singlell:
    def __init__(self, head=None):
        self.head = head
    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head is not None:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insertAtStart(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertAtMiddle(self,value,x):
        temp = Node(value)
        t1 = self.head
        while t1.next is not None:
            if (t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def deletell(self,value):
        t1 = self.head
        prev = t1
        if t1.data == value:
            self.head = t1.next

        while t1.next is not None:
            if t1.data == value:
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next
        if t1.data == value:
            prev.next =None
        
    def display(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data, end=" -> ")
            t1 = t1.next
        print("None")

obj = Singlell()

obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtStart(5)
obj.insertAtMiddle(40,20)
obj.deletell(30)
obj.deletell(5)
obj.deletell(40)
obj.display()