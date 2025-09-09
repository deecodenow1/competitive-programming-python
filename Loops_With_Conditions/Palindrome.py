num = int(input("Enter a number: "))
rev = 0
n = num

if(num>=0):
    while(n>0):
        rem = n % 10
        rev = rev*10 + rem
        n = n // 10
    if(rev==num):
        print("Yes")
    else:
        print("No")
else:
    print("Enter a positive number.")