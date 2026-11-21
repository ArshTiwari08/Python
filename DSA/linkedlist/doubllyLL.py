class Node:
    def __init__(self, value= None):
        self.data = value
        self.next = None
        self.prev = None

class doublyLL:
    def __init__(self):
        self.head = None

    def insertAtEnd(self,value):
        temp = Node(value)
        if self.head is None:
            self .head = temp
            return
        t = self.head
        while t.next is not None:
            t = t.next
        t.next = temp
        temp.prev = t

    def insertAtStart(self,value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insertAtmiddle(self,value,position):
        t = self.head
        while t.next is not None:
            if t.data == position:
                break
            t = t.next
        temp = Node(value)
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t

    def deleteel(self,value):
        if self.head == None:
            print(" Linked list is Empty")
            return
        t = self.head
        if t.data == value:
            self.head = t.next
            self.head.prev = None
            return
        while t.next is not None:
            if t.data == value:
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            t = t.next
        if t.data == value:
            t.prev.next = None

    
    def display(self):
        t1 = self.head
        while t1.next is not None:
            print(t1.data,end="<->")
            t1 = t1.next
        print(t1.data)

obj = doublyLL()

obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtStart(5)
obj.insertAtmiddle(80,20)
obj.deleteel(5)
obj.deleteel(80)
obj.deleteel(40)


obj.display()