class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def clear(self):
        self.root = None

    def search(self, x):
        return self._search(self.root, x)

    def _search(self, node, x):
        if node == None:
            return None
        if x == node.value:
            return node
        if x < node.value:
            return self._search(node.left, x)
        else:
            return self._search(node.right, x)

    def insert(self, x):
        if self.root == None:
            self.root = Node(x)
        else:
            self._insert(self.root, x)

    def _insert(self, node, x):
        if x < node.value:
            if node.left == None:
                node.left = Node(x)
                node.left.parent = node
            else:
                self._insert(node.left, x)
        elif x > node.value:
            if node.right == None:
                node.right = Node(x)
                node.right.parent = node
            else:
                self._insert(node.right, x)

    def breadth(self):
        if self.root == None:
            return
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.value, end=' ')
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, node):
        if node == None:
            return
        print(node.value, end=' ')
        self._preorder(node.left)
        self._preorder(node.right)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node == None:
            return
        self._inorder(node.left)
        print(node.value, end=' ')
        self._inorder(node.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, node):
        if node == None:
            return
        self._postorder(node.left)
        self._postorder(node.right)
        print(node.value, end=' ')

    def count(self):
        return self._count(self.root)

    def _count(self, node ):
        if node == None:
            return 0
        return 1 + self._count(node.left) + self._count(node.right)
    
    def dele(self, x):
        self.root = self._dele(self.root, x)

    def _dele(self, node, x):
        if node == None:
            return None
        if x < node.value:
            node.left = self._dele(node.left, x)
        elif x > node.value:
            node.right = self._dele(node.right, x)
        else:
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            else:
                node.value = self._min(node.right).value
                node.right = self._dele(node.right, node.value)
        return node
    
    def min(self):
        return self._min(self.root).value
    
    def _min(self, node):
        if node.left == None:
            return node
        return self._min(node.left)
    
    def max(self):
        return self._max(self.root).value
    
    def _max(self, node):
        if node.right == None:
            return node
        return self._max(node.right)
    
    def sum(self):
        return self._sum(self.root)
    
    def _sum(self, node):
        if node == None:
            return 0
        return node.value + self._sum(node.left) + self._sum(node.right)
    
    def avg(self):
        return self.sum() / self.count()
    
    def height(self):
        return self._height(self.root)
    
    def _height(self, node):
        if node == None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))
    
    def cost(self):
        return self._cost(self.root)
    
    def _cost(self, node):
        if node == None:
            return 0
        return node.value + max(self._cost(node.left), self._cost(node.right))
    
    def isAVL(self):
        return self._isAVL(self.root)
    
    def _isAVL(self, node):
        if node == None:
            return True
        if abs(self._height(node.left) - self._height(node.right)) > 1:
            return False
        return self._isAVL(node.left) and self._isAVL(node.right)
    
    def print(self):
        self._print(self.root)

    def _print(self, node):
        if node == None:
            return
        print(node.value, end=' ')
        self._print(node.left)
        self._print(node.right)

tree = BinarySearchTree()
input()
n = int(input())
arr = list(map(int, input().split()))
if(n == 5):
    for i in arr:
        tree.insert(i)
    tree.breadth()
elif(n == 6):
    for i in arr:
        tree.insert(i)
    tree.preorder()
elif(n == 7):
    for i in arr:
        tree.insert(i)
    tree.inorder()
elif(n == 8):
    for i in arr:
        tree.insert(i)
    tree.postorder()
elif(n == 9):
    for i in arr:
        tree.insert(i)
    print(tree.count())
elif(n == 11):
    for i in arr:
        tree.insert(i)
    print(tree.min())
elif(n == 12):
    for i in arr:
        tree.insert(i)
    print(tree.max())
