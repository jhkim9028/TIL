x = int(input())

dp = [i for i in range(x+1)]
a = [i for i in range(x+1)]
dp[1] = 0
a[1] = 0

for i in range(2,x+1):
    dp[i] = dp[i-1]+1
    a[i] = i - 1
    
    if not i % 3 and dp[i] > dp[i//3]+1:
        dp[i] = dp[i//3] + 1
        a[i] = i // 3

    if not i % 2 and dp[i] > dp[i//2]+1:
        dp[i] = dp[i//2] + 1
        a[i] = i // 2


print(dp[x])
print(x, end=' ')
b = a[x]
for i in range(dp[x]):
    print(b,end=' ')
    b = a[b]