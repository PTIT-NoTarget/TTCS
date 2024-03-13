for i in range(4):
    input()

dict1 = {}

for i in range(2):
  key, value = input().split(":")
  dict1[key] = value

s = input()
print(s,":",dict1[s])