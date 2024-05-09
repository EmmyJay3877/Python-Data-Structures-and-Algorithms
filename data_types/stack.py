"""
Stacks: Last-in-first-out
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self, value):
        if not self.is_empty():
            popped_node = self.top.value
            self.top = self.top.next
            return popped_node

    def is_empty(self):
        return self.top is None