n = int(input("Enter a number: "))
count = 0
i = 0

while(n!=0):
    n = n//10
    i+=1

print(i)