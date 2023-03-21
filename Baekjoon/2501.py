N, K = map(int, input().split())

ans = []

for i in range(1,int(N**0.5+1)):
    if not  N % i:
        ans.append(i)
    else:
        continue

for i in range(len(ans)):
    if N // ans[i] in ans:
        continue
    ans.append(N // ans[i])

ans.sort()
if len(ans) < K:
    print(0)
else:
    print(ans[K-1])

# N, K = map(int, input().split())

# ans = []

# for i in range(1, N+1):
#     if not N % i:
#         ans.append(i)

# print(ans[K-1])