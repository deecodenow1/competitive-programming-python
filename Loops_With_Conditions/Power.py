a = int(input("Enter a number: "))
b = int(input("Enter power to the entered number: "))
result = 1

for i in range(0, b):
    result = result * a

print(result)