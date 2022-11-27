import sys

class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
def isSum_Binary_Tree(root):

    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.key
 
    left = isSum_Binary_Tree(root.left)
    right = isSum_Binary_Tree(root.right)

    if left != -sys.maxsize and right != -sys.maxsize and root.key == left + right:
        return 2 * root.key
 
    return -sys.maxsize
 
 
if __name__ == '__main__':
 
    root = Node(44)
    root.left = Node(9)
    root.right = Node(13)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
 
    if isSum_Binary_Tree(root) != -sys.maxsize:
        print('Binary tree is a sum Binary tree')
    else:
        print('Binary tree is not a sum Binary tree')
 