n = 5

for i in range(n, 0, -1):
    for k in range(n-i):
        print("_", end="")
    for j in range(i):
        print("*", end="")
    print()
