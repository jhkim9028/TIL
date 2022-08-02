# x = 각 자리가 등차
# N는 주어진다. x는 1과 N사이 수
# x의 개수를 출력

# 일단 이중반복문을 돌리고 겉에는 N을 안에는 문자열로 받아서 조건문으로 

# 110
N = int(input())

hansu = 0
for n in range(1,N+1):
        if n < 100:
            hansu += 1
        elif int(str(n)[1]) - int(str(n)[0]) == int(str(n)[2]) - int(str(n)[1]):
            hansu += 1
print(hansu)