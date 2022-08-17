import sys
sys.stdin = open('1764_input.txt')

n, m = map(int,input().split())

dict_ = {}
name = [input() for _ in range(n+m)]
for i in name:
    dict_[i] = 0
for i in name:
    dict_[i] += 1
ans = []
for k, v in dict_.items():
    if v == 2:
        ans.append(k)
        
print(len(ans))
ans.sort()
for a in ans:
    print(a)
