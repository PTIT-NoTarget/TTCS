
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def addToHead(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def addToTail(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last = self.head
    while(last.next):
      last = last.next
    last.next = new_node

  def addAfter(self, prev_node, data):
    if prev_node is None:
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def traverse(self):
    temp = self.head
    while(temp):
      print(temp.data, end=" ")
      temp = temp.next

  def deleteFromHead(self):
    temp = self.head
    self.head = self.head.next
    return temp.data

  def deleteFromTail(self):
    temp = self.head
    while(temp.next.next):
      temp = temp.next
    last = temp.next
    temp.next = None
    return last.data

  def deleteAfter(self, prev_node):
    temp = prev_node.next
    prev_node.next = prev_node.next.next
    return temp.data

  def dele(self, data):
    temp = self.head
    if temp is not None:
      if temp.data == data:
        self.head = temp.next
        temp = None
        return
    while temp is not None:
      if temp.data == data:
        break
      prev = temp
      temp = temp.next
    if temp == None:
      return
    prev.next = temp.next
    temp = None

  def search_val(self, data):
    temp = self.head
    while(temp):
      if temp.data == data:
        return temp
      temp = temp.next
    return None
  
  def search_val_bef(self, data):
    temp = self.head
    while(temp):
      if temp.next.data == data:
        return temp
      temp = temp.next
    return None

  def count(self):
    temp = self.head
    count = 0
    while(temp):
      count += 1
      temp = temp.next
    return count

  def dele_i(self, i):
    temp = self.head
    if i == 0:
      self.head = temp.next
      temp = None
      return
    for _ in range(i-2):
      temp = temp.next

    if temp is None or temp.next is None: 
      return
    next = temp.next.next
    temp.next = None
    temp.next = next

  def sort(self):
    temp = self.head
    while(temp):
      temp2 = temp.next
      while(temp2):
        if temp.data > temp2.data:
          temp.data, temp2.data = temp2.data, temp.data
        temp2 = temp2.next
      temp = temp.next

  def dele_p(self, p):
    temp = self.head
    if temp == p:
      self.head = temp.next
      temp = None
      return
    while(temp.next != p):
      temp = temp.next
    temp.next = p.next
    p = None

  def toArray(self):
    temp = self.head
    arr = []
    while(temp):
      arr.append(temp.data)
      temp = temp.next
    return arr

  def merge(self, llist):
    temp = self.head
    while(temp.next):
      temp = temp.next
    temp.next = llist.head

  def addBefore(self, prev_node, data):
    following = prev_node.next
    new_node = Node(data)
    prev_node.next = new_node
    new_node.next = following

  def attach(self, llist):
    temp = self.head
    while(temp.next):
      temp = temp.next
    temp.next = llist.head

  def max(self):
    temp = self.head
    max = temp.data
    while(temp):
      if temp.data > max:
        max = temp.data
      temp = temp.next
    return max

  def min(self):
    temp = self.head
    min = temp.data
    while(temp):
      if temp.data < min:
        min = temp.data
      temp = temp.next
    return min

  def sum(self):
    temp = self.head
    sum = 0
    while(temp):
      sum += temp.data
      temp = temp.next
    return sum

  def avg(self):
    temp = self.head
    sum = 0
    count = 0
    while(temp):
      sum += temp.data
      count += 1
      temp = temp.next
    return sum/count

  def sorted(self):
    temp = self.head
    while(temp.next):
      if temp.data > temp.next.data:
        return False
      temp = temp.next
    return True

  def insert(self, data):
    temp = self.head
    if temp is None:
      self.head = Node(data)
      return
    if temp.data > data:
      new_node = Node(data)
      new_node.next = temp
      self.head = new_node
      return
    while(temp.next is not None and temp.next.data < data):
      temp = temp.next
    new_node = Node(data)
    new_node.next = temp.next
    temp.next = new_node

  def reverse(self):
    prev = None
    current = self.head
    while(current is not None):
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev

  def same(self, llist):
    self.sort()
    llist.sort()
    temp1 = self.head
    temp2 = llist.head
    while(temp1 and temp2):
      if temp1.data != temp2.data:
        return "no"
      temp1 = temp1.next
      temp2 = temp2.next
    if temp1 is None and temp2 is None:
      return "yes"
    return "no"

  def printList(self, check = 1):
    arr = []
    temp = self.head
    while(temp):
      arr.append(temp.data)
      temp = temp.next
    for i in arr:
      print(i, end="")
      if i != arr[-1]:
        print(" ", end="")
    if check == 1:
      print()

input()
section = input()

llist = LinkedList()

if section == "1":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  val = int(input())
  print(f'1. Add {val} before the head of {n}-element list: ', end="")
  llist.printList()
  llist.addToHead(val)
  llist.printList()
elif section == "2":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  val = int(input())
  print(f'2. Add {val} after the tail of {n}-element list: ', end="")
  llist.printList()
  llist.addToTail(val)
  llist.printList()
elif section == "3":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  pos, val = map(int, input().split())
  print(f'3. Insert an element {val} after the element {pos} in the {n}-element list ', end="")
  llist.printList()
  llist.addAfter(llist.search_val(pos), val)
  llist.printList()
elif section == "4":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  print(f'4. Traverse the {n}-element list: ', end="")
  llist.printList()
  llist.traverse()
elif section == "5":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  print(f'5. Delete the head of the {n}-element list: ', end="")
  llist.printList()
  llist.deleteFromHead()
  llist.printList()
elif section == "6":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  print(f'6. Delete the tail of the {n}-element list: ', end="")
  llist.printList()
  llist.deleteFromTail()
  llist.printList()
elif section == "7":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  pos = int(input())
  print(f'7. Delete the element after the element {pos} of the {n}-element list: ', end="")
  llist.printList()
  llist.deleteAfter(llist.search_val(pos))
  llist.printList()
elif section == "8":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  val = int(input())
  print(f'8. Delete the element {val} in the {n}-element list: ', end="")
  llist.printList()
  llist.dele(val)
  llist.printList()
elif section == "9":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  val = int(input())
  print(f'9. Search the element {val} in the {n}-element list: ', end="")
  llist.printList()
  print(llist.search_val(val).data)
elif section == "10":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  print(f'10. Count the number of the elements of the {n}-element list: ', end="")
  llist.printList()
  print(llist.count())
elif section == "11":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  pos = int(input())
  print(f'11. Delete the {pos}rd element in the {n}-node list: ', end="")
  llist.printList()
  llist.dele_i(pos)
  llist.printList()
elif section == "12":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  print(f'12. Sort in accending order the {n}-node list: ', end="")
  llist.printList()
  llist.sort()
  llist.printList()
elif section == "13":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  pos = int(input())
  print(f'13. Delete the element {pos} in the {n}-node list: ', end="")
  llist.printList()
  llist.dele_p(llist.search_val(pos))
  llist.printList()
elif section == "14":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  print(f'14. create and return array containing info of all nodes in the {n}-node list. ', end="\n")
  llist.printList()
elif section == "15":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  n2 = int(input())
  llist2 = LinkedList()
  for _ in input().split():
    llist2.addToTail(int(_))
  print(f'15. Merge two ordered doubly linked lists of integers into one ordered list: {n}-node list = ', end="")
  llist.printList(0)
  print(f'; {n2}-node list: ', end="")
  llist2.printList()
  llist.merge(llist2)
  llist.sort()  
  llist.printList()
elif section == "16":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  val, pos = map(int, input().split())
  print(f'16. add a node with value {val} before the node {pos} in the {n}-node list: ', end="")
  llist.printList(0)
  print(".")
  llist.addBefore(llist.search_val_bef(pos), val)
  llist.printList()
elif section == "17":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  n2 = int(input())
  llist2 = LinkedList()
  for _ in input().split():
    llist2.addToTail(int(_))
  print(f'17. Attach a doubly linked list of {n2} elements ', end="")
  llist2.printList(0)
  print(f' to the end of another doubly linked list of {n} nodes: ', end="")
  llist.printList()
  llist.attach(llist2)
  llist.printList()
elif section == "18":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  print(f'18. find and return the maximum value in the {n}-node list: ', end="")
  llist.printList()
  print(llist.max())
elif section == "19":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  print(f'19. find and return the minimum value in the {n}-node list: ', end="")
  llist.printList()
  print(llist.min())
elif section == "20":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  print(f'20. return the sum of all values in the {n}-node list: ', end="")
  llist.printList()
  print(llist.sum())
elif section == "21":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  print(f'21. return the average of all values in the {n}-node list: ', end="")
  llist.printList()
  print("{:.2f}".format(llist.avg()))
elif section == "22":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  print(f'22. check and return true if the {n}-node list ', end="")
  llist.printList(0)
  print(" is sorted, return false if the list is not sorted.")
  print(str(llist.sorted()).lower())
elif section == "23":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  val = int(input())
  print(f'23. sort the 19-node list: ', end="")
  llist.printList(0)
  print(f' then insert a node with value {val} into the sorted list so that the new list is a sorted list ')
  llist.sort()
  llist.printList()
  llist.insert(val)
  llist.printList()
elif section == "24":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  print(f'24. Reverse the doubly linked list of {n} nodes: ', end="")
  llist.printList()
  llist.reverse()
  llist.printList()
elif section == "25":
  n = int(input())
  for _ in input().split():
    llist.addToTail(int(_))
  n2 = int(input())
  llist2 = LinkedList()
  for _ in input().split():
    llist2.addToTail(int(_))
  print(f'25. Check whether two doubly linked list have the same contents: 1st list of {n} elements: ', end="")
  llist.printList(0)
  print(f'; 2nd list of {n2} elements: ', end="")
  llist2.printList()
  print(llist.same(llist2))
