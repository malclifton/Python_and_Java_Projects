#Malia Clifton
#Lab 05
# Problem 1: Find the sum of digits of a positive number using recursion.

def digitSum(n):
    if n==0:
        return 0
    return (n % 10 + digitSum(int(n/10)))
    
num1= int(input("Enter a positive integer: "))
sum= digitSum(num1)
print("The sum of the entered integer " + str(num1) + " is " + str(sum))

#Problem 2: Given a set of positive integers and a target sum, find all subsets of the set that add up to the target sum. Solve it using both recursion and without recursion to solve this

def printAllSubsets(arr, n, sum, p=[]):
    if sum == 0:
        print(p)
        return
    if n == 0 or sum < 0:
        return
    p.append(arr[n - 1])
    printAllSubsets(arr, n - 1, sum - arr[n - 1], p)
    p.pop()  
    printAllSubsets(arr, n - 1, sum, p)

def printAllSubsets2 (arr,sum):
    dp = [[] for _ in range(sum + 1)]
    dp[0]= [[]]
    for arr in arr:
        for i in range(sum,arr-1,1):
            for subset in dp[i-arr]:
                dp[i].append(subset+[arr])
               
    return dp[sum]
   
    

arr1= (input("Enter the values for your list: ").split(','))
n=len(arr1)
arr= [int(x) for x in arr1]
sum1=input("Enter the value of your target: ")
sum=int(sum1)
printAllSubsets(arr, n, sum)
printAllSubsets2(arr,sum)
