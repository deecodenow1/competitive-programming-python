n = 5

for i in range(n):
    for j in range(1, n+1):
        if(j==n or j==1):
            print("*", end="")
        else:
            print("_", end="")
    print()
