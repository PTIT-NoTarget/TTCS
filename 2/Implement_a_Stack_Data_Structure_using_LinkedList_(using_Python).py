class Stack:
  def __init__(self):
    self.list = []
    self.size = 0

  def push(self, value):
    self.list.append(value)
    self.size += 1

  def pop(self):
    if self.size == 0:
      return "Error: Stack is empty"
    self.size -= 1
    return self.list.pop()
  
  def top(self):
    if self.size == 0:
      return "Error: Stack is empty"
    return self.list[-1]
  
  def __str__(self):
    return " ".join(map(str, self.list))
  
  def __len__(self):
    return self.size
  
stack = Stack()
input()
case = int(input())
if(case == 1):
  n = int(input())
  for i in input().split():
    stack.push(int(i))
  print("1. Push 10 to the top of 10-element stack:", stack)
  stack.push(10)
  print("Current stack:", stack)
elif(case == 2):
  n = int(input())
  for i in input().split():
    stack.push(int(i))
  print("2. Pop the top element of 10-element stack:", stack)
  print(stack.pop())
  print("Current stack:", stack)
elif(case == 3):
  print("3. Pop empty stack")
  print(stack.pop())
elif(case == 4):
  n = int(input())
  for i in input().split():
    stack.push(int(i))
  print("4. Top of 10-element stack:", stack)
  print(stack.top())
  print("Current stack:", stack)
elif(case == 5):
  n = int(input())
  for i in input().split():
    stack.push(int(i))
  print("5. After 5 operations on the 10-element stack:", stack)
  for i in range(int(input())):
    s = input()
    if(s == "pop"):
      stack.pop()
    else:
      stack.push(int(s.split()[1]))
  print("Current stack size:", len(stack))
  print("Current stack:", stack)

