import sys
sys.stdin = open('7785_input.txt')

T = int(input())

dict_ = {}
for t in range(T):
    man, inout = map(str, input().split())
    if inout == 'enter':
        dict_[man] = 1
    elif inout == 'leave':
        dict_[man] = 0
ans = []
for k, v in dict_.items():
    if v == 1:
        ans.append(k)
ans.sort(reverse=True)
for a in ans:
    print(a)