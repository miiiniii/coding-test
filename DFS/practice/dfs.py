"""
preorder: Node -> Left -> Right
inorder: Left -> Node -> Right
postorder: Left -> Right -> Node
"""

def preorder(node):
    if node is None:
        return
    print(node.value, end=' ')  # 한 줄에 공백으로 출력
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return 
    inorder(node.left)
    print(node.value, end=' ')
    inorder(node.right)


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end=' ')



class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)


preorder(root)