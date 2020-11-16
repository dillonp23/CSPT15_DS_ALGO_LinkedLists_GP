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