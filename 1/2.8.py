def func(list):
  return (min(list), max(list))

list = []
while True:
  try:
    list.append(int(input()))
  except EOFError:
    break

a, b = func(list)
print(a, b)