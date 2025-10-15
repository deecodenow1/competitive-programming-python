A = input()
A = A + A
result = ''

for i in range(0, len(A)):
    if (A[i] == A[i].upper()):
        continue
    elif (A[i] == 'a' or A[i] == 'e' or A[i] == 'i' or A[i] == 'o' or A[i] == 'u'):
        result += '#'
    else:
        result += A[i]

print(result)
