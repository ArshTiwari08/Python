class Stack:

    # 1. Constructor
    def __init__(self):
        self.items = []

    # 2. Check whether stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # 3. Push element into stack
    def push(self, item):
        self.items.append(item)

    # 4. Remove top element
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    # 5. Return top element without removing it
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    # 6. Return stack size
    def size(self):
        return len(self.items)

    # 7. Display stack elements
    def display(self):
        print("Stack (top -> bottom):", self.items[::-1])


# Main program
s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)

print("After pushing elements:")

s.display()

print("Is stack empty?", s.is_empty())
print("Stack size:", s.size())
print("Top element:", s.peek())