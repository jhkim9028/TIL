# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

n = input()
n =int(n)
a = 1

while True:
    print(n-a)
    a += 1
    if (n - a) == -1:
        break