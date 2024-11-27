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
