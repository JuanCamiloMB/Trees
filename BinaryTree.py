class Node:
    def __init__(self, data, left_child = None, right_child = None):
        self.data = data
        self.left = left_child
        self.right = right_child

class Tree:
    def __init__(self, root_value):
        self.root = Node(root_value)
    
    def height(self, root, left_height = 0, right_height = 0):
        if root == None:
            return max(left_height, right_height)
        left_height = height(root.left)
        right_height = height(root.right)
        return 1 + max(left_height, right_height)
    
    def leftHeight(self, root):
        return self.height(root.left_child)

    def rightHeight(self, root):
        return self.height(root.right_child)

    def isBalanced(self, root = self.root):
        if (self.leftHeight(root) - self.rightHeight(root)) in [-1, 0, 1]:
            return True
        return False