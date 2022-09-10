N = int(input())
group_word = N
for n in range(N):
    word = input()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            group_word -= 1
print(group_word)