import sys
input = sys.stdin.readline

T = int(input())
flag = True

dic = {}
ans = 0
for t in range(T):
    chat = input().strip()
    if chat == 'ENTER':
        if flag:
            flag = False
            continue
        else:
            ans += len(dic)
            dic = {}
            continue

    if not flag:
        dic[chat] = 1

ans += len(dic)
print(ans)