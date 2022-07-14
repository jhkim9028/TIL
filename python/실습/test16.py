word = input()

vowel = ['a', 'e', 'i', 'o', 'u']
num = -1
count = 0

for i in vowel:
    num += 1
    for k in word:
        if i == k:
            count += 1
print(count)