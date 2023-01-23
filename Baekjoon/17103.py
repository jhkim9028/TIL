# 에라토스테네스 체
# pypy3

a = 10 ** 6

che = [False, False] + [True] * (a - 1)

# 에라토스테네스 체
for i in range(2, int(a ** 0.5) + 1):
    if che[i]:
        for j in range(2 * i, a + 1, i):
            che[j] = False

T = int(input())

for t in range(T):
    N = int(input())

    cnt = 0
    for n in range(1,N+1):
        if che[n]:
            if che[N-n]:
                cnt += 1

    if cnt % 2:
        print(cnt // 2 + 1)
    else:
        print(cnt // 2)