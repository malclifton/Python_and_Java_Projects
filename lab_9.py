#Lab9 Problem 1
#Write a program to implement the operations of stack. Show all the operations of a stack such as push, pop, peek/top, and to check if the stack is empty or not
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)
        print(data, "pushed to stack")

    def pop(self):
        if not self.is_empty():
            data = self.stack.pop()
            print(data, "popped from stack")
        else:
            print("Invalid: stack is empty")

    def peek(self):
        if not self.is_empty():
            data1 = self.stack[-1]
            print(data1, "is at the top of the stack")
        else:
            print("Invalid: stack is empty")

stack = Stack()
quit = False
while not quit:
    input1 = input("Enter an operation --> pop, push, peek, empty, or quit: ").lower()
    
    if input1 == "pop":
        stack.pop()
    elif input1 == "push":
        i = input("Enter a value: ")
        stack.push(i)
    elif input1 == "peek":
        stack.peek()
    elif input1 == "empty":
        if stack.is_empty():
            print("The stack is empty")
        else:
            print("The stack is not empty")
    elif input1 == "quit":
        quit = True
