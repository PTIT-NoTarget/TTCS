def chia(x, y):
  if y == 0:
    return "Cannot divide by 0.\nNone"
  return x/y

print(chia(int(input()), int(input())))