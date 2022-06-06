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

    def Balance(self, root = self.root):
        if root == None:
            return True
        left_height = self.leftHeight(root.left)
        right_height = self.rightHeight(root.right)
        if left_height - right_height not in [-1, 0, 1]:
            return False
        return self.Balance(root.left) and Balance(root.right)

    def byArray(self, array, root, contador = 0):
        if len(array) > 0:
            if contador == 0:
                self.root = Node(array[0])
                contador += 1
                root = self.root
                del array[0]
                self.byArray(array, root, contador)
            
            if array[0] > root.data:
                if root.right != None:
                    root.right = Node(array[0])
                    contador += 1
                    del array[0]
                    self.byArray(array, root, contador)
            
                else:
                    self.byArray(array, root.right)
            
            if array[0] < root.data:
                if root.left != None:
                    root.left = Node(array[0])
                    contador += 1
                    del array[0]
                    self.byArray(array, root, contador)
            
                else:
                    self.byArray(array, root.left)