n = int(input("Enter a number: "))
digit = 0

while (n!=0) :
    num=n%10
    digit = digit + num
    n//=10

print(digit)