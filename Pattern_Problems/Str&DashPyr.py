n = 5

for i in range(n, 0, -1):
    print("*", end="")
    for j in range(i):
        print("_", end="")
    print("*")
