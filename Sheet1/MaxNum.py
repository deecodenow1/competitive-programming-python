# Program to find the maximum of three integers without using max()

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    maximum = a
elif b >= c:
    maximum = b
else:
    maximum = c

print("The maximum number is:", maximum)
