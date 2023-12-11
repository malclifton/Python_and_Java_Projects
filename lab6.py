"""
    Malia Clifton 
    Lab 06
    10/11/23
"""
#Problem 1
def ascendSort(nums):
    if len(nums) > 1:
        r = len(nums)//2
        L = nums[:r]
        M = nums[r:]
        ascendSort(L)
        ascendSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            nums[k] = M[j]
            j += 1
            k += 1
        

a= (input("Enter the values in your array seperated by a comma: ").split(','))
arr = [int(x) for x in a]
ascendSort(arr)
for i in range(len(arr)):
   print(arr[i], end=" ")
print("\n\n\n")

#Problem 2 
def mergeSort(num1,num2,m,n):
 num3=[0]*(m+n) 
 k=0
 l=0
 for i in range(m+n):
  if k>(m-1):
   num3[i]=num2[l]
   l+=1
  elif num1[k]<= num2[l]:
   num3[i]=num1[k]
   k+=1
  else:
   num3[i]=num2[l]
   l+=1
 return num3
  
  
 
 

a1= (input("Enter the values for your first array: ").split(','))
arr1=[int(x) for x in a1]
m=int((input("Enter the number of elements you want to be merged from your array: ")))
num1=arr1[:m]

a2=(input("Enter the values for your second array: ").split(','))
arr2=[int(x) for x in a2]
n=int((input("Enter the number of elements you want to be merged from your array: ")))
num2=arr2[:n]

print(mergeSort(num1,num2,m,n))