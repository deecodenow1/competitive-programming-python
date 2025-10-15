T = int(input())
vowels = 'aeiou'

for i in range(T):
    str = input()

    countVowel = 0
    countConso = 0

    for ch in str:
        if ch.lower() in vowels:
            countVowel += 1
        else:
            countConso += 1

    print(countVowel, countConso)
