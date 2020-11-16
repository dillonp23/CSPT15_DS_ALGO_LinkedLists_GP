"""
Here we will outline a few concepts in comments and code.
"""

# Creating linked lists in python:

# 1. Start with a Node class
class Node:
    # Node initializer
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# 2. LinkedList class and init:
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = Node(data)

        if self.head:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node
        else:
            self.head = new_node


a = Node(1)
llist = LinkedList(a)
llist.append(2)
llist.append(3)

print(llist.head)
print(llist.head.data)

print(llist.head.next)
print(llist.head.next.data)

print(llist.head.next.next)
print(llist.head.next.next.data)