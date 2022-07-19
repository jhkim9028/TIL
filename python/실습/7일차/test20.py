# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

number = int(input())

cnt = 0
a = []
while number != 0:
    number //= 10
    cnt += 1
    a.append(cnt)
print(sum(a))
