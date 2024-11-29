# Creating Array
from array import *
a1= array('i', [1,2,3,4,5,6])


# Insertion 
a1.insert(1, 7)
print(a1)    
# output - (1,7,2,3,4,5,6)


# Traversal 
 for i in a1:
   print(i)
 # output- 1 7 2 3 4 5 6


#linear search 
def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i]== target:
      return i
  else:
    return -1

print(linear_search(a1, 9)) 
# output- -1

