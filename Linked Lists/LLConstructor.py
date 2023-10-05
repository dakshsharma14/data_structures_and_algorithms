class node:
    # only thing it contains is node constructor
    # node is going to  contain value and next
    def __init__(self, value):
        self.value = value
        self.next = None


class LL:
    # this is a LL constructor, value as a parameter
    # create new node
    def __init__(self, value):
        # this line will call the node class and create the node
        new_node = node(value)

        self.head = new_node
        self.tail = new_node
        self.length = 1


# from this we have created a node with head and tail
my_linked_list = LL(4)

print(my_linked_list.head.value)


# # create new node and Add to the end
# def append(self,value):
#
# # create the new node and add to the start
# def prepend(self, value):
#
# def insert(self, index, value):


# any one of those above methods wants to create a node
# they can call this class\


##############################################################

# LL: Constructor
# You are tasked with implementing a basic data structure: a singly linked list.
#
# To accomplish this, you will create two classes, Node and LinkedList.
#
# The Node class will represent an individual node within the linked list, while the LinkedList class will manage the
# overall list structure.
#
# Your implementation should satisfy the following requirements:
#
#
#
# Create a Node class with the following features:
#
# A constructor that takes a value as an argument and initializes the value attribute of the node.
#
# A next attribute, initialized to None, which will store a reference to the next node in the list.
#
# Create a LinkedList class with the following features:
#
# A constructor that takes a value as an argument, creates a new Node with that value, and initializes the head and
# tail attributes of the linked list to point to the new node.
#
# A length attribute, initialized to 1, which represents the current number of nodes in the list.
class Node:
    def __init__(self, value):
        self.value = value
        # this will store reference to the nexg node
        self.next = None


class LinkedList:
    # takes in value as an argument
    def __init__(self, value):
        new = Node(value)
        self.head = new
        self.tail = new
        self.length = 1
