x = int(input("Enter starting number: "))
y = int(input("Enter ending number: "))

def Sqr(x, y):
    for i in range(x, y+1):
        ans = i**2
        print(ans)

Sqr(x, y)
