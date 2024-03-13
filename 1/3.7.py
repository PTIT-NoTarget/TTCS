def is_anagram(s1, s2):
  s1 = "".join([i for i in s1 if i.isalnum()]).lower()
  s2 = "".join([i for i in s2 if i.isalnum()]).lower()
  return sorted(s1) == sorted(s2)

s1 = input()
s2 = input()
print(str(is_anagram(s1, s2)).lower())
