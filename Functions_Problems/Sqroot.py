import math

A = int(input("Enter a number: "))

def Sqroot(num):
    ans = math.sqrt(num)
    if ans.is_integer():
        print(int(ans))
    else:
        print(-1)

Sqroot(A)
