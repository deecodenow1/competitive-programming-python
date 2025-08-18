# Program to find the maximum of two numbers

A = float(input("Enter number A: "))
B = float(input("Enter number B: "))

if A > B:
    print("The maximum number is:", A)
elif B > A:
    print("The maximum number is:", B)
else:
    print("Both numbers are equal:", A)
