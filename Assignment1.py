""" 
    Malia Clifton
    CSC 2720
    Programming Assignment 1
    10/01/23
"""


#Word Analysis
def  minWordLength(list):
    if not list:
        return 0
    min=len(list[0])
    for i in list:
        if len(i)<min:
             min=len(i)
    return min

def maxWordLength(list):
    if not list:
         return 0
    max=len(list[0])
    for i in list:
        if len(i)>max:
             max=len(i)
    return max

def wordLengthRange(list):
     if not list:
         return 0
     return max(list)-min(list)

def averageWordLength(list):
     total=sum(len(i) for i in list )
     return total/len(list)

def mostCommonWordLength(list):
     mcount=0
     for i in range(len(list)):
         count=0
         for j in range(len(list)):
             if len(list[j])==len(list[i]):
                  count+=1
                  if count>mcount:
                      mcount = count
     if mcount>1:
          return mcount
     else:
         return -1 
         
print("Please type max,range,average, or mode. Then enter the amount of words followed by your choice of words.")
operation = input().strip().upper()
clist = int(input())
list=[input() for _ in range(clist)]
if operation == "MIN":
        print(minWordLength(list))
elif operation == "MAX":
        print(maxWordLength(list))
elif operation == "RANGE":
        print(wordLengthRange(list))
elif operation == "AVERAGE":
        print(averageWordLength(list))
elif operation == "MODE":
        print(mostCommonWordLength(list))
else:
        print("Invalid input")


#Bubble Sort
def bubbleSort(arr):
    ccount=0
    scount=0
    for i in range(len(arr)):
	    for j in range (0,len(arr)-i-1): 
              ccount+=1
              if arr[j]>arr[j+1]:
                  scount+=1
                  temp=arr[j]
                  arr[j]=arr[j+1]
                  arr[j+1]=temp
    return ccount, scount

print("\n\n\n")
print("(2).Bubble Sort")
a= (input("Enter the values for your array: ").split(','))
arr = [int(x) for x in a]
print("(Number of comparisons, Number of swaps)")
print(bubbleSort(arr))
print("Sorted Array: ")
for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
print("\n\n\n")


#String Permutation
def stringPerm(string):
    if len(string) == 0:
        return [""]
    f = string[0]
    r = string[1:]
    p = []
    for i in stringPerm(r):
        for j in range(len(i) + 1):
            p.append(i[:j] + f + i[j:])
    return p

print("(2).Bubble Sort")
string = input("Enter your string: ")
p = stringPerm(string)
for i in p:
    print(i)



