a = 10 ** 5

che = [False,False] + [True] * (a-1)

for i in range(2, int(a**0.5)+1):
    if che[i]:
        for j in range(2*i, a+1, i):
            che[j] = False


T = int(input())

for t in range(T):
    b = int(input())

    q = b // 2
    w = q
    
    for i in range(a):
        if che[q] and che[w]:
            print(q, w)
            break
        q -= 1
        w += 1

