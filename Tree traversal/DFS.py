"""
Depth First Search: Explores a tree by going as deep as possible
along one branch before backtracking.

Three types of DFS algo include:
1. Inorder
2. Preorder
3. Postorder 
"""

"""
Inorder_traversal: An algorithm that recursively performs an inorder
traversal on the left subtree, visits the root node, and finally
performs an inorder traversal on the right subtree.

left child -----> root node -----> right child
"""
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)


"""
Preorder_traversal: This algorithm visits the root node first, then
recursively performs a preorder traversal on the left subtree, and finally 
on the right subtree.

root node -----> left child -----> right child
"""
def preorder_traversal(node):
    if node is not None:
        print(node.value, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

"""
Postorder_traversal: This algorithm recursivly performs a postorder traversal
on the left subtree, then on the right subtree, and finally on the root node.

left child -----> right child -----> root node
"""
def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=" ")