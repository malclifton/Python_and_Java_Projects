#Assignment 2 Program 1
#Determine if a word is a palindrome with a stack or a queue
#A palindrome is the same backwards and forwards  ex: racecar, mom, pop

class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
    
def palindrome(user):
    user=user.lower()
    s=Stack()
    for character in user:
        s.push(character)
    reversed_string = ""
    while not s.is_empty():
        reversed_string = reversed_string + s.pop()
    return user == reversed_string
   
while True:
    user = input("Enter a string or q: ")
    if user.lower() == 'q':
        break
    elif palindrome(user):
        print('THe string is a palindrome.')
    else:
        print('The string is not a palindrome.')
 