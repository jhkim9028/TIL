from re import A
import sys

sys.stdin = open("1926_input.txt", "r")


# for i in range(1, N+1):
#     if '3' in str(i):
#         print('-',end=' ')
#     elif '6' in str(i):
#         print('-', end=' ')
#     elif '9' in str(i):
#         print('-', end=' ')    
#     else:
#         print(i, end=' ')



N = int(input())


clap = ['3', '6', '9']
for i in range(1, N+1):
    cnt = 0
    for j in str(i):
        if j in clap:
            cnt += 1
    if cnt > 0:
        i = '-' * cnt
    print(i, end=' ')