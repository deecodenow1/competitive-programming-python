a = int(input("Enter a number: "))
sum = 0

if(a>0):
    for i in range(1, a):
        if(i%2 != 0):
            sum = sum + i
    print(sum)
else:
    print("Enter a positive number.")
