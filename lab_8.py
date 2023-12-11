#Malia CLifton
#Lab 08

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None   

    def insertList(self, data):     #method to add nodes to the linked list (by user input)
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node  

    def reverseList(self):          #method to reverse the order of a linked list (Problem 1)
        p = None
        current = self.head
        while current:
            n = current.next
            current.next = p
            p = current
            current = n
        self.head = p

    def printList(self):            #method to print out the linked list
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("Null")

print("Problem 1: Write a program to return the reverse of a single linked list.")
list = LinkedList()

i = int(input("\nEnter the number of nodes: "))
for _ in range(i):
    data = int(input("\tEnter a value: "))
    list.insertList(data)
print("Linked List: ")
list.printList()

print("Reversed Linked List: ")
list.reverseList()
list.printList()

print("\n\n\n\nProblem 2: Create a loop in the linked list and find where the loop begins.")

loop_start_index = int(input("\nEnter the index for where the loop starts: "))
#creates the loop at the index provided by the user and then identifies the integer at said index.
current = list.head
loop_node = None
index = 0
while current:
    if index == loop_start_index:
        loop_node = current
    if index == i - 1:
        last_node = current
    current = current.next
    index += 1
if loop_node:
    last_node.next = loop_node
    print("Loop begins at:", loop_node.data)
else:
    print("ERROR")


