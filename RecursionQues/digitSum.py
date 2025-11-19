def digit(n):
    if (n == 0):
        return 0
    return n%10 + digit(n//10)

num = int(input("Enter number: "))
print(digit(num))
