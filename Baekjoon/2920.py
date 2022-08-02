# 1~ 8
num = list(map(int, input().split()))
# print(num) [1, 2, 3, 4, 5, 6, 7, 8]

if num == sorted(num):
    print('ascending')
elif num == sorted(num, reverse = True):
    print('descending')
else:
    print('mixed')    