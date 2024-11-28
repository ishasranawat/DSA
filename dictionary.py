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

          ### Dictionary Methods ###
my_dict= {
    'apple':'sweet',
    'orange':'sour',
    'watermelon':{'one':"1",'two':'2','three':'3'}
}

# 1.copy
my_dict.copy()
print(my_dict)
# OP {'apple': 'sweet', 'orange': 'sour', 'watermelon': {'one': '1', 'two': '2', 'three': '3'}}


# 2.get
op=my_dict.get('apple')
print(op)
# OP sweet


# 3.list items
dict_itmes=my_dict.items()
print(dict_itmes)
#  OP dict_items([('apple', 'sweet'), ('orange', 'sour'), ('watermelon', {'one': '1', 'two': '2', 'three': '3'})])



# 4. list keys
dict_keys= my_dict.keys()
print(dict_keys)
#  OP dict_keys(['apple', 'orange', 'watermelon'])



# 5. set pair
dict_setdefault= my_dict.setdefault('lemon','zesty')
print(my_dict)
#OP  {'apple': 'sweet', 'orange': 'sour', 'watermelon': {'one': '1', 'two': '2', 'three': '3'}, 'lemon': 'zesty'}

# 6.Update (add a new dictionary to existing)
new_dict= {
    'peas':'green',
    'raddish':'white',
}
dict_update= my_dict.update(new_dict)
print(my_dict)
# OP {'apple': 'sweet', 'orange': 'sour', 'watermelon': {'one': '1', 'two': '2', 'three': '3'}, 'lemon': 'zesty', 'peas': 'green', 'raddish': 'white'}


