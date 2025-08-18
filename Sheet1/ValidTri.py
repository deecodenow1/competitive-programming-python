# Program to check if three angles form a valid triangle

A = int(input("Enter angle A (in degrees): "))
B = int(input("Enter angle B (in degrees): "))
C = int(input("Enter angle C (in degrees): "))

if A > 0 and B > 0 and C > 0 and (A + B + C) == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
