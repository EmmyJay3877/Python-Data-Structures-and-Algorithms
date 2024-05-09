"""
Tree: is a data structure that represents 
hierarchical tree structure with a set of connected nodes
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.right == None
        self.left == None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return

        temp = self.root
        while temp:
            if value < temp.value:
                if temp.left is None:
                    temp.left = Node(value)
                    return
                else:
                    temp = temp.left
            elif value > temp.value:
                if temp.right is None:
                    temp.right = Node(value)
                    return
                else:
                    temp = temp.right
            else:
                return

    def search(self, value):
        temp = self.root
        while temp:
            if temp.value == value:
                return temp
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return None