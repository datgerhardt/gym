class Node(object):
    def __init__(self, val) -> None:
        self.val = val 
        self.left = None
        self.right = None
        
    def insert_left(self, child):
        if self.left is None:
            self.left = child
        else:
            child.left = self.left
            self.left = child
    def insert_right(self, child):
        if self.right is None:
            self.right = child
        else:
            child.right = self.right
            self.right = child


if __name__ == "__main__":
    root = Node('a')
    print(root.val)
    print(root.left)

    root.insert_left(Node("b"))
    print(root.left)
    print(root.left.val)

    root.insert_right(Node("c"))
    print(root.right)
    print(root.right.val)
   
