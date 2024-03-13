def Prime(n):
  if n < 2:
    return "Not a prime"
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return "Not a prime"
  return "Prime"

def func(n):
  s1 = n * (n - 1) // 2
  s2 = 1
  for i in range(1, n):
    s2 *= i
  s3 = 0
  for i in range(1, n):
    s3 += 1/i
  return "%d\n%d\n%.2f\n%s" % (s1, s2, s3, Prime(n))

print(func(int(input())))