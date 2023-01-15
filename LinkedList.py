class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        while(cur_node.next!= None):
            cur_node = cur_node.next
        cur_node.next = new_node

    def length(self):
        cur_node = self.head
        total = 0
        while(cur_node.next!=None):
            total+=1
            cur_node= cur_node.next
        print(total)
    
    def display(self):
        elements = []
        cur_node = self.head
        while(cur_node.next!=None):
            cur_node= cur_node.next
            elements.append(cur_node.data)
            
        print(elements)

my_list = LinkedList()
my_list.append(1)
my_list.display()