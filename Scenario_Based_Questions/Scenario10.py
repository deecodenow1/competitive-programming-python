n = int(input())
arr = list(map(int, input().split()))
unique = []

for i in range(n):
    count = 0
    for j in range(n):
        if(arr[i] == arr[j]):
            count += 1

    if(count == 1):
        unique.append(arr[i])

if (len(unique) == 0):
    print(-1)
else:
    print(unique)
