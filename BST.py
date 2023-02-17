class BinarySearchTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, data):
        if data == self.data:
            return True
        
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def inorder_traversal(self):
        elements = []

        if self.left:
            elements += self.left.inorder_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    def add_child(self, data):
        if self.data == data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    elements = [4,6,8,2,1,5,7,3,3,1]
    root = build_tree(elements)
    print(root.inorder_traversal())
    print(root.search(7))
