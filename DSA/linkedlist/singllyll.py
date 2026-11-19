class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next


class singlyLinkedlist:
    def __init__(self, head=None):
        self.head = head

    # Insert at End
    def insertAtEnd(self, value):
        temp = Node(value)

        if self.head is not None:
            t1 = self.head

            while t1.next is not None:
                t1 = t1.next

            t1.next = temp
        else:
            self.head = temp

    # Insert at Start
    def insertAtStart(self, value):
        temp = Node(value)

        temp.next = self.head
        self.head = temp

    # Insert at Middle
    def insertAtMiddle(self, value, position):

        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            self.insertAtStart(value)
            return

        temp = Node(value)
        t1 = self.head

        for i in range(position - 1):
            if t1 is None:
                print("Position out of range")
                return
            t1 = t1.next

        if t1 is None:
            print("Position out of range")
            return

        temp.next = t1.next
        t1.next = temp

    # Delete at Start
    def deleteAtStart(self):

        if self.head is None:
            print("Linked List is empty")
            return

        self.head = self.head.next

    # Delete at End
    def deleteAtEnd(self):

        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        t1 = self.head

        while t1.next.next is not None:
            t1 = t1.next

        t1.next = None

    # Delete at Middle (position-based, 0-indexed)
    def deleteAtMiddle(self, position):

        if position < 0 or self.head is None:
            print("Invalid position or empty Linked List")
            return

        if position == 0:
            self.deleteAtStart()
            return

        t1 = self.head

        for i in range(position - 1):

            if t1.next is None:
                print("Position out of range")
                return

            t1 = t1.next

        if t1.next is None:
            print("Position out of range")
            return

        t1.next = t1.next.next

    # Display Linked List
    def print_linkedlist(self):

        t1 = self.head

        while t1 is not None:
            print(t1.data, end=" -> ")
            t1 = t1.next

        print("None")


# Creating Linked List
obj = singlyLinkedlist()

# Insertion
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)

print("Original Linked List:")
obj.print_linkedlist()

# Insert at Start
obj.insertAtStart(5)

# Insert at Middle
obj.insertAtMiddle(25, 3)

print("\nAfter Insertion:")
obj.print_linkedlist()

# Delete at Start
obj.deleteAtStart()

# Delete at End
obj.deleteAtEnd()

# Delete at Middle
obj.deleteAtMiddle(2)

print("\nAfter Deletion:")
obj.print_linkedlist()