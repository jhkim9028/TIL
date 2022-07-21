word = input()
num = -1
none = 0

for alphabet in word:
    num += 1
    if alphabet == 'a':
        print(num)
        break
for alphabet in word:
    none += 1
    if alphabet == 'a':
        break
    elif none == num + 1 :    
        print('-1')

# word = input()
# # 처음 등장하는 a의 위치
# # word 길이만큼 반복해서 a가 처음 등장하는 위치구함
# cnt = 0
# for j in range(0,len(word)):
#     if word[j] != 'a':
#         cnt += 1
#         if cnt == len(word):
#             print('-1')
#     elif word[j] == 'a':
#         print(j)
#         break
    


#추가문제
for i in word:
    num += 1
    if i == 'a':
        print(num)