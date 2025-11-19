n = int(input())
count = 0

for i in range(0, n):
    arr = list(map(int, input().split()))
    marks = arr[0]
    attendance = arr[1]
    if (marks>=75):
        if (attendance >= 80):
            count += 1

print(count)
