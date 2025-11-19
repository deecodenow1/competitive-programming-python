def revNum(n):
    if n == 0:
        return
    print(n, end=" ")
    revNum(n-1)

N = int(input())
revNum(N)
