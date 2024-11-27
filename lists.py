# Access List 
list= ['a', 'b', 'c']

print(list[1])
# op- b

# Traverse
for i in list:
  print(i)
# op- a, b, c


# insert
list.insert(0,'f')
print(list)
# ['f', 'a', 'b', 'c']


# append
list.append('j')
print(list)
# ['f', 'a', 'b', 'c', 'j']


# extend
newlist= ['w','p','o']
list.extend(newlist)
print(list)
# ['f', 'a', 'b', 'c', 'j', 'w', 'p', 'o']


# pop 
list.pop()
print(list)
# op- ['a', 'b']


# remove
list.remove('a')
print(list)
#op- ['b','c']


# delete
del list[0:2]
print(list)
#op- []

# linear search
def linear_search(list,target):
    for i in list:
        if target in range(len(list)):
            return "Target found"
        else:
            return "Target not found"
            
print(linear_search([1,2,4,6,4,3],78))


# ** Delimeter** Convert string to a list 
a= 'hello,hello,hello'
delimeter= ','
b= a.split(delimeter)
print(b)

# op- ['hello', 'hello', 'hello']
