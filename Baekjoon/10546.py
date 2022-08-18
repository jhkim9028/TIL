import sys
sys.stdin = open('10546_input.txt')

dict_ = {}
n = int(input())
cnt = 0
while cnt != n + n-1:
    name = input()
    cnt += 1
    if name not in dict_:
        dict_[name] = 1
    else:
        dict_[name] += 1
for k, v in dict_.items():
    if v % 2 == 1:
        print(k)