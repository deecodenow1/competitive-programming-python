n = int(input("Enter a number: "))
rev = 0

while (n!=0) :
    num = n%10
    rev = rev*10 + num
    n//=10

print(rev)