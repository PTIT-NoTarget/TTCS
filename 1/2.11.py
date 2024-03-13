try:
  a = int(input())
  if(a < 0):
    print("Error: not a number")
  else:
    print(bin(a)[2:])
    sum = 0
    for i in str(a):
      sum += int(i)
    print(sum)
    print(str(a)[::-1])
except ValueError:
  print("Error: negative number")