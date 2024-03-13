list = []
while True:
  try:
    list.append(int(input()))
  except EOFError:
    break

for i in reversed(list):
  print(i, end=' ')
print()
for i in list:
  if i > 500:
    break
  if i > 150:
    continue
  if i % 5 == 0:
    print(i, end=' ')