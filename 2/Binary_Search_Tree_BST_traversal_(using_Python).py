class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right == None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def breadth(self):
        self._breadth(self.root)

    def _breadth(self, node):
        if node == None:
            return
        queue = []
        queue.append(node)
        while len(queue) > 0:
            print(queue[0].value, end='  ')
            node = queue.pop(0)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, node):
        if node == None:
            return
        print(node.value, end='  ')
        self._preorder(node.left)
        self._preorder(node.right)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node == None:
            return
        self._inorder(node.left)
        print(node.value, end='  ')
        self._inorder(node.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, node):
        if node == None:
            return
        self._postorder(node.left)
        self._postorder(node.right)
        print(node.value, end='  ')

tree = BinarySearchTree()
input()
case = int(input())
if(case == 1):
    n = int(input())
    for i in input().split():
        tree.insert(int(i))
    print("1. Test breadth-first traversal:")
    tree.breadth()
elif(case == 2):
    n = int(input())
    for i in input().split():
        tree.insert(int(i))
    print("2. Test pre-order traversal:")
    tree.preorder()
elif(case == 3):
    n = int(input())
    for i in input().split():
        tree.insert(int(i))
    print("3. Test in-order traversal:")
    tree.inorder()
elif(case == 4):
    n = int(input())
    for i in input().split():
        tree.insert(int(i))
    print("4. Test post-order traversal:")
    tree.postorder()

