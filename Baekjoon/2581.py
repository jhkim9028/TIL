# 2581
m = int(input())
n = int(input())

# 에라토스테네스 체
che = [False,False] + [True] * (n-1)

for i in range(2,int(n**0.5)+1):
    if che[i]:
        for j in range(2*i,n+1,i):
            che[j] = False

# 소수의 합
hap = []

for i in range(m,n+1):
    if che[i]:
        hap.append(i)

# 범위 안에 소수가 없으면
if not len(hap):
    print(-1)
else:
    print(sum(hap))
    print(hap[0])