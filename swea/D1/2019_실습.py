import sys

sys.stdin = open("2019_input.txt", "r")

N = int(input()) # 8

a = 0

for i in range(0,N+1):
    a = 1 * 2**i
    print(a, end=' ')