
dict1 = dict()
dict2 = dict()
str_dict1 = input()
for i in range(3):
  key, value = input().split(" : ")
  dict1[key] = value

str_dict2 = input()
for i in range(3):
  key, value = input().split(" : ")
  dict2[key] = value

print(str_dict1)
for key, value in dict1.items():
  print(key, ":", value)

print(str_dict2)
for key, value in dict2.items():
  if key not in dict1:
    print(key, ":", value)
