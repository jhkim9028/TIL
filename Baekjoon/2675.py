T = int(input())
ans = []

for t in range(T):
    new = ''
    sen = list(input().split())
    for i in range(len(sen[-1])):
        new += sen[-1][i] * int(sen[0])
    ans.append(new)
for a in ans:
    print(a)