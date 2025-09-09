n = int(input("Enter a positive number: "))

if(n>0):
    for i in range(1, n+1):
        print(i, end=" ")
else:
    print("Enter a positive number.")