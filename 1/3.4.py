def func1(s1, s2):
  pos1 = len(s1) // 2 - 2
  pos2 = len(s2) // 2 - 2
  return "1. " + s1[pos1:pos1 + 4] + " " + s2[pos2:pos2 + 4]

def func2(s1,s2):
  pos1 = len(s1) // 2
  return "2. " + s1[:pos1] + s2 + s1[pos1:]

def func3(s1, s2):
  return "3. " + s1[0] + s2[0] + s1[len(s1) - 1] + s2[len(s2) - 1]

def func4(s):
  list = []
  for i in s:
    if i.islower():
      list.append(i)
  for i in s:
    if i.isupper():
      list.append(i)
  for i in s:
    if i.isdigit():
      list.append(i)
  for i in s:
    if not i.isalnum():
      list.append(i)
  return "".join(list)

def func5(s):
  list = [0, 0, 0]
  for i in s:
    if i.isalpha():
      list[0] += 1
  for i in s:
    if i.isdigit():
      list[1] += 1
  for i in s:
    if not i.isalnum():
      list[2] += 1
  return "%d %d %d" % (list[0], list[1], list[2])

s1 = input()
s2 = input()

print(func1(s1, s2))
print(func2(s1, s2))
print(func3(s1, s2))
print("4. " + func4(s1) + " " + func4(s2))
print("5. " + func5(s1) + " " + func5(s2))