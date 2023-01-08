# 1676

N = int(input())

ans = 1
cnt = 0
for n in range(1,N+1):
    ans *= n

for i in str(ans)[::-1]:
    if i == '0' :
        cnt += 1
    else:
        break
print(cnt)