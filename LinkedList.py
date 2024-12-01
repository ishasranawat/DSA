1.# Create a Linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head
        self.length = 1
        


2.# Insertion at the beginning
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def prepend(self, value):
        new_node= Node(value)
        new_node.next=self.head
        self.head=new_node
        self.length+=1



3.# Insertion at the end 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head= new_node
            self.tail= new_node
            self.length+=1 
        else:
            self.tail.next= new_node
            self.tail=new_node
            self.length+=1
 




















            
