N = int(input())

group = N

for n in range(N):
    word = input()
    list_ = []
    for i in range(len(word)-1):
        # 앞 뒤 두개 비교
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                group -= 1
                break
print(group)