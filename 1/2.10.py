import math

def gcd(a,b):
  return math.gcd(a,b)

def lcm(a,b):
  return a*b//math.gcd(a,b)

def isPrime(n):
  if n < 1:
    return False
  if(n == 1):
    return True
  for i in range(2, int(math.sqrt(n))+1):
    if n%i == 0:
      return False
  return True

def prime(a,b):
  list = []
  for i in range(1, min(a,b)):
    if a%i == 0 and b%i == 0 and isPrime(i):
      list.append(i)
  return list

a = int(input())
b = int(input())
for i in prime(a,b):
  print(i, end=' ')
print(gcd(a,b))
print(lcm(a,b))

