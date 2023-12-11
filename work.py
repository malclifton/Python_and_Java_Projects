
#Malia Clifton
#09/20/23
#Lab 4/ Problem 3
#Problem 3: Write a python program to implement the binary search algorithm to find an element in a sorted list. Also, tell it’s space and time complexity of your program.

def binarySearch(arr, target):
    left = 0              
    right = len(arr) - 1 
    
    while left <= right: 
        mid = (left + right) // 2
        mid_value = arr[mid] 
        if mid_value == target:   
            return mid             
        elif mid_value < target:     
            left = mid + 1           
        else:                      
            right = mid - 1       
    return -1 
     
a= (input("Enter the values for your list: ").split(','))
sorted_array = [int(x) for x in a]
sorted_array.sort()
n=(input("Enter the value of your target: "))
n=int(n)
t = binarySearch(sorted_array,n)
print("Original list : " + str(sorted_array))
if t!=-1:
    print("Binary search for target " + str(n)+ " is at index " + str(t))
else:
    print("That number isn't in the array")
  
print("The Big O notation time complexity is O(log n) and the space complexity is O(1).")
