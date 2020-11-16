"""
Given only a reference to a specific node in a linked list, delete that node from a singly-linked list.
Example:
The code below should first construct a linked list (x -> y -> z) and then delete `y` from the linked list by calling the function `delete_node`. It is your job to write the `delete_node` function.
```python
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None
x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')
x.next = y
y.next = z
delete_node(y)
```
*Note: We can do this in O(1) time and space! But be aware that our solution will have some side effects...*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def delete_node(delete_this_node):
    # Your code here
    next = delete_this_node.next

    if next:
        delete_this_node.value = next.value
        delete_this_node.next = next.next

    else:
        # We're at the end of the list so write an exception (just for the purposes of this demo we're only deleting within the middle of a list)
        raise Exception("This technique does not work for the last node of the list")

    pass


x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

print(x)
print(x.value)
print(x.next.value)

print(y)
print(y.value)
print(y.next.value)

print(z)
print(z.value)

delete_node(y)

print(x)
print(x.value)
print(x.next.value)

print(y)
print(y.value)