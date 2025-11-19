n = int(input())
arr = list(map(int, input().split()))
ans = []

for i in arr:
    if (i%5 == 0):
        ans.append(i)

ans.reverse()

if(len(ans) == 0):
    print(-1)
else:
    for i in ans:
        print(i, end=" ")
