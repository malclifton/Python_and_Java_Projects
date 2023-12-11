"""
Malia Clifton
Lab 02
09-06-23

"""
import random
list=random.sample(range(1,50),7)
list1=sorted(list)
print("The values of the list are " + str(list))

maximum=max(list1)
print("(a) The max of the sorted list is "+ str(maximum))
#The time complexity of this problem is O(n) and the space complexity is O(1)

m= len(list1)//2
mid=list1[m]+list1[~m]/2
print('(b) The median of this sorted list of odd length is ' + str(mid))
#The time complexity of this problem is O(n) and the space complexity is O(1)

r=max(list)-min(list)
print('(c) The range of the unsorted list is ' + str(r))
#The time complexity is O(n) and the space complexity is O(n)