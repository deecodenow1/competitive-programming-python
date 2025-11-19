def palin(s):
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return palin(s[1:-1])

S = input().strip()

if palin(S):
    print("Palindrome")
else:
    print("Not Palindrome")
