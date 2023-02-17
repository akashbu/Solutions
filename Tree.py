class TreeNode:

    def __init__(self, data):
        self.data= data
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        p = self.parent
        level = 0
        while p:
            level +=1
            p = p.parent
        return level

    def print_tree(self):
        
        spaces = " "*self.get_level()*3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    


def build_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('HP'))
    laptop.add_child(TreeNode('Dell'))

    grocery = TreeNode('Grocery')
    grocery.add_child(TreeNode('Apple'))
    grocery.add_child(TreeNode('Banana'))

    root.add_child(laptop)
    root.add_child(grocery)
    return root

if __name__ == '__main__':
    root = build_tree()
    root.print_tree()   
    pass