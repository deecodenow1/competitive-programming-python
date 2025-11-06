N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
    for j in range(i, N):
        output = []
        for k in range(i, j+1):
            output.append(arr[k])
        print(sum(output))
