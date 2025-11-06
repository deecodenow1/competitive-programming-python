N = int(input())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in range(len(arr2)):
    l = arr2[0]
    r = arr2[1]

add = sum(arr[l-1:r-1])

print(add)
