import math

P = float(input("Enter Perpendicular length: "))
B = float(input("Enter Base length: "))

def pytha(p, b):
    ans = math.sqrt(p**2 + b**2)
    return ans

H = pytha(P, B)
print("The Hypotenuse is:", H)
