#3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

list =[a, b, c]

for i in list:
    if i % 2 == 0:
        print(i)