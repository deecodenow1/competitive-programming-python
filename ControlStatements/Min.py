# Program to find the minimum of three numbers

A = float(input("Enter number A: "))
B = float(input("Enter number B: "))
C = float(input("Enter number C: "))

min = A

if B < min:
    min = B

if C < min:
    min = C

print("The minimum number is:", min)
