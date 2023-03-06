N, K = map(int, input().split())

on = list(map(int, input().split()))


ans = []
ans.append(sum(on[0:K]))

for i in range(N-K):
    ans.append(ans[i]-on[i]+on[i+K])
    
    
print(max(ans))
