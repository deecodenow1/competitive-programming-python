A = input()
B = int(input())

for i in range(len(A)):
    if(A[i] == chr(B)):
        print(i)
        break
