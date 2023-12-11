
#Malia Clifton
#09/20/23
#Lab 4/ Problem 3
#Problem 2: Write a problem to calculate the factorial of a number and find its big O notation of time and space complexity.

def calcFact (num):
    if (num == 0):
        return 1
    return num * calcFact(num-1)

n=(input("Enter the value of your number: "))
n=int(n)
print("The factorial of " + str(n) + " is " + str(calcFact(n)))
print("The Big O notation time complexity is O(n) and the space complexity is O(n).")
