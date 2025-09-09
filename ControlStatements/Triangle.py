# Program to determine the type of triangle based on angles

angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))
angle3 = int(input("Enter third angle: "))

if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("It is a Right Triangle.")
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        print("It is an Obtuse Triangle.")
    else:
        print("It is an Acute Triangle.")
else:
    print("The angles do not form a valid triangle.")
