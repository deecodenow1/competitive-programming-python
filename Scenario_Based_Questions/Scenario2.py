n = int(input("Enter number of employees: "))
id = list(map(int, input().split()))
even = 0

for i in id:
    if (i%2 == 0):
        print(i)
        even += 1
    else:
        continue

if (even == 0):
    print(-1)
