import sys
sys.stdin = open('1204_input.txt')

T = int(input())

for t in range(T):
    dict_ = {}
    n = int(input())
    number = list(map(int, input().split()))
    for num in number:
        if num not in dict_:
            dict_[num] = 1
        if num in dict_:
            dict_[num] += 1
    for k, v in dict_.items():
        if v == max(dict_.values()):
            print(f'#{n} {k}')