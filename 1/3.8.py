def func(s):
  if s.isalnum():
    return int(s, 16)
  else:
    return "String is not in Hexadecimal"

s = input()
print(func(s))