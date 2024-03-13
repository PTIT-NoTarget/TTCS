s = "\"" + input() + "\""

arr = [int(i) for i in input().split(", ")]

sub_tup = "(" + input() + ")"
print("(", sep='', end='')
print(s, arr, sub_tup, sep=', ', end='')
print(")", sep='', end='')
print()
print(arr[1], end='')

