import math

a = int(input())
b = int(input())
c = int(input())
if(a == 0):
    if(b == 0):
        if(c == 0):
            print("The equation has no real root.")
        else:
            print("The equation has no real root.")
    else:
        print("%.2f" % (-c / b))
else:
    delta = b * b - 4 * a * c
    if(delta < 0):
        print("The equation has no real root.")
    else:
        a1 = (-b + math.sqrt(delta)) / (2 * a)
        a2 = (-b - math.sqrt(delta)) / (2 * a)
        if(a1 > a2):
            a1, a2 = a2, a1
        print("%.2f %.2f" % (a1, a2))
