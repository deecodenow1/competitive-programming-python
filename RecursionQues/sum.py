def add(n):
    if (n==0):
        return 0
    return add(n-1) + n

N = int(input())
print(add(N))
