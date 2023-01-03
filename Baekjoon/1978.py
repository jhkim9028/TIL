# 1978

N = int(input())

num = list(map(int, input().split()))

# 소수 = 1과 자기 자신만 약수
# 소수 개수
cnt = 0
for n in num:
    measure = []
    if n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        continue
    for i in range(1,n+1):
        if n % i == 0:
            measure.append(n//i)
    if len(measure) == 2:
        cnt += 1
print(cnt)