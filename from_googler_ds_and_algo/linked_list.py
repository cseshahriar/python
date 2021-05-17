# Linked List
""" head=[1]-[3]-[5] link every node(single linked list)

head=[1]-><-[3]-><-[5]
double linked list

link is connection
"""

class Node:

    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value

class DoubleLinkedList:

    def __init__(self):
        self.head = None # list first node
        self.tail = None # list last  node
        self.size = 0

    def add(self)