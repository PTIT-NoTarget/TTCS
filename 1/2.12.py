def palindroms(m,n):
  for i in range(m,n+1):
    if str(i) == str(i)[::-1]:
      print(i)
palindroms(int(input()),int(input()))