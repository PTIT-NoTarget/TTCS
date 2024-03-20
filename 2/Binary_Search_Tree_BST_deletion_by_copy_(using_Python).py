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
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left == None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        elif value > node.value:
            if node.right == None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)

    def delete(self, value):
        self.root = self._delete(value, self.root)

    def _delete(self, value, node):
        if node == None:
            return None
        if value < node.value:
            node.left = self._delete(value, node.left)
        elif value > node.value:
            node.right = self._delete(value, node.right)
        else:
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            else:
                node.value = self._find_max(node.left).value
                node.left = self._delete(node.value, node.left)
        return node

    def _find_max(self, node):
        while node.right != None:
            node = node.right
        return node

    def breadth(self):
        if self.root == None:
            return
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            print(queue[0].value, end='  ')
            node = queue.pop(0)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

bst = BinarySearchTree()
input()
n = int(input())
arr = list(map(int, input().split()))
for i in arr:
    bst.insert(i)
de = int(input())
print('Breadth-first traversal of the original BST:')
bst.breadth()
print()
print('Breadth-first traversal after deleting node', de, ':')
bst.delete(de)
bst.breadth()
print()

