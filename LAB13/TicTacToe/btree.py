from btnode import Node

class LinkedBinaryTree:
    def __init__(self, value):
        self.key = Node(value)


    def insert_left(self, new_node):
        if self.get_left_child() == None:
            self.key.left_child = Node(new_node)


    def insert_right(self, new_node):
        if self.get_right_child() == None:
            self.key.right_child = Node(new_node)


    def get_right_child(self):
        return self.key.right_child


    def get_left_child(self):
        return self.key.left_child


    def set_root_val(self, obj):
        self.key.value = obj


    def get_root_val(self):
        return self.key.value


    def preorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()


    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.key)
        if self.right_child:
            self.right_child.inorder()


    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.key)