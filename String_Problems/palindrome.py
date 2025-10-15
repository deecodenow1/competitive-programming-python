T = int(input())

for i in range(T):
    str = input()
    rev = ""
        
    for r in range(len(str)-1, -1, -1):
        rev += str[r]

    if (str == rev):
        print(1)
    else:
        print(0)
