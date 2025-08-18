# WAP to check if the last digit is 4.

Num = int(input("Enter a Number : "))

if (abs(Num%10)==4):
    print(Num,"contains 4 at it's last.")
else:
    print(Num,"does'nt contains 4 at it's last.")