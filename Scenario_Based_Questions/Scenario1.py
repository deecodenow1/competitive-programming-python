n = int(input())
arr = list(map(int, input().split()))
fail = 0
passed = 0

for i in range(n):
    if(arr[i]<35):
        fail += 1
    elif(arr[i]>=35):
        passed+=1

print(passed, fail)
