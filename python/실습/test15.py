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

#추가문제
for i in word:
    num += 1
    if i == 'a':
        print(num)