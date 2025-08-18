# Program to check if a number is divisible by both 5 and 11

A = int(input("Enter an integer A: "))

if A % 5 == 0 and A % 11 == 0:
    print("The number is divisible by both 5 and 11.")
else:
    print("The number is NOT divisible by both 5 and 11.")
