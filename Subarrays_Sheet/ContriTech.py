N = int(input())
arr = list(map(int, input().split()))
result = 0

for i in range(N):
    formula = arr[i]*(i+1)*(N-i)
    result += formula

print(result)
