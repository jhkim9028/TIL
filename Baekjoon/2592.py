import sys
sys.stdin = open('2592_input.txt')

num = [int(input()) for _ in range(10)]

avg = sum(num) / 10
print(int(avg))

dict_ = {}

for i in num:
    dict_[i] = num.count(i)

for k, v in dict_.items():
    if v == max(dict_.values()):
        print(k)