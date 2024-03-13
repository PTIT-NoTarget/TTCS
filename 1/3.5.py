def func1(s):
  ans = ""
  for i in s:
    if i.isdigit():
      ans += i
  return "1. " + ans

def func2(s):
  ans = ""
  for i in s.split():
    if not i.isalnum() and len(i) == 1:
      continue
    else:
      for j in i:
        if not j.isalnum():
          i = i.replace(j, "")
      ans += i + " "
  return "2. " + ans[:-1]

def func3(s):
  ans = ""
  for i in s.split(" - "):
      ans += i + " "
  return "3. " + ans[:-1]
s = input()
print(func1(s))
print(func2(s))
print(func3(s))