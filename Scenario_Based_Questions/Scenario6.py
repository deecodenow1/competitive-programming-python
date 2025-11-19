n = int(input())
arr = list(map(int, input().split()))
count = 0
maximum = 0

for i in range(n):
    if(arr[i] == 0):
        count += 1
    elif(arr[i] == 1):
        if (count >= maximum):
            maximum = count
            count = 0

print(maximum)
