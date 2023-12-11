#1.)Given a sorted array of non-negative integers, find the first missing element
#My given array {0,1,2,3,4,6,7,8,9}

#Linear Search
def linear_list(list,a,b):
    if a>b:
        return[]
    if a not in list:
        return [a] + linear_list(list,a+1,b)
    return linear_list(list,a+1,b)

#Binary Search
def binary_list(list):
    left=0
    right=len(list)
    mid=(left+right)//2
    while left<right:
        mid=(left+right)//2
        if list[mid]>mid:
            right=mid
        else:
            left=mid+1
    return left



list=[0,1,2,3,4,6,7,8,9]
a=list[0]
b=list[-1]
print("The given list is [0,1,2,3,4,6,7,8,9].")
print("The first missing integer using linear search is "+str(linear_list(list,a,b)))
print("The first missing integer using binary search is "+str(binary_list(list)))
