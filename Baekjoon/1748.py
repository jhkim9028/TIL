# 1748

N = int(input())

long = len(str(N))

# 예) 120에서 100 ~ 120까지 개수
a = N - (10 ** (long-1)) + 1

b = 0
if long != 1:
    for i in range(1,long):
        b += ((10 ** i) - (10 ** (i-1))) * i

ans = a * long + b
print(ans)