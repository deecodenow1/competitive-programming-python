n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
avg = total/n

ans = 0
for j in arr:
    if j > avg:
        ans += 1

print(ans)
