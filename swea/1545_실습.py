import sys

sys.stdin = open("1545_input.txt", "r")

T = int(input())
b = 0
for i in range(T+1):
    b = T - i
    print(b, end=' ')