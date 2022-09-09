sen = input()
cnt = 0
cnt2 = 0
for s in sen:
    if s == ' ':
        cnt += 1

if sen[0] == ' ' and sen[-1] == ' ':
    print(cnt - 1)
elif sen[0] == ' ' or sen[-1] == ' ':
    print(cnt)
else:
    print(cnt + 1)