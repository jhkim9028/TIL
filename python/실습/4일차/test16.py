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

# word = input()
# # 모음 갯수
# # 모음 리스트를 만들고

# a = ['a', 'e', 'i', 'o', 'u']
# cnt = 0
# # for문 모음 돌리고 if문 a가 있다면 +1
# for i in a:
#     if i in word:
#         cnt += 1
# print(cnt)