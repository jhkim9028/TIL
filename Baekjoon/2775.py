T = int(input())

for t in range(T):
    #  층
    k = int(input())

    # 호
    n = int(input())
    
    ans = []
    a = [i for i in range(1,n+1)]
    ans.append(a)

    for i in range(k-1):
        a = [1]
        for j in range(n-1):
            a.append(a[j]+ans[i][j+1])
        ans.append(a)
    print(sum(ans[-1]))