class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    root,head = None, None
    def BToDll(self, root:Node):
        if root is None:
            return
        #Recursively convert right subtree
        self.BToDll(root.right)
        #Insert root into doubly linked list
        root.right = self.head
        #change left pointer of previous head
        if self.head is not None:
            self.head.left = root
        #change head of doubly linked list
        self.head = root
        #Recursively convert left subtree
        self.BToDll(root.left)
    @staticmethod
    def print_list(head:Node):
        print("Extracted double linked list:")
        while head is not None:
            print(head.data, end = ' ')
            head = head.right
tree = BinaryTree() 
tree.root = Node(5) 
tree.root.left = Node(3) 
tree.root.right = Node(6) 
tree.root.left.left = Node(1) 
tree.root.left.right = Node(4) 
tree.root.right.right = Node(8) 
tree.root.left.left.left = Node(0) 
tree.root.left.left.right = Node(2) 
tree.root.right.right.left = Node(7) 
tree.root.right.right.right = Node(9) 

tree.BToDll(tree.root) 
tree.print_list(tree.head) 
            
