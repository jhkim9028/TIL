# 에라토스테네스 체

N, K = map(int, input().split())

che = [False,False] + [True] * (N-1)

a = []
for i in range(2,N+1):
    if che[i]:
        a.append(i)
        for j in range(2*i, N+1, i):
            if not che[j]:
                pass
            else:
                che[j] = False
                a.append(j)


print(a[K-1])