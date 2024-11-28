# Create a dictionary 
my_dict= {
    'apple':'sweet',
    'orange':'sour',
    'watermelon':{'one':"1",'two':'2','three':'3'}
}
print(my_dict)
# to get the keys
print(my_dict.keys())


# adding a pair
my_dict['strawberry']='pretty'
print(my_dict)


# traversal 
def print_dict(my_dict):
    for key in my_dict:
        print(key, my_dict[key])
print_dict(my_dict)


# searching 
def search(my_dict, value):
    for key in my_dict:
        if my_dict[key] == value:
            return key 
    return -1  
print(search(my_dict, 'sweet'))  # Output: apple
print(search(my_dict, 'apple'))  # Output: -1 
print(search(my_dict, {'one': "1", 'two': '2', 'three': '3'}))  # Output: watermelon


# **removing pairs**

my_dict.pop('apple')
print(my_dict)    
# OP {'orange': 'sour', 'watermelon': {'one': '1', 'two': '2', 'three': '3'}}

my_dict.popitem()
print(my_dict)
# OP {'apple': 'sweet', 'orange': 'sour'}

del my_dict['watermelon']
print(my_dict)
# OP {'apple': 'sweet', 'orange': 'sour'}

my_dict.clear()
print(my_dict)
# OP {}

