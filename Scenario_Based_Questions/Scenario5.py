n = int(input())
arr = list(map(int, input().split()))
k = int(input())

sum = 0

for i in range(n):
    for j in range(i+1, n):
        s = arr[i] + arr[j]
        if (s == k):
            sum = sum + 1

print(sum)
