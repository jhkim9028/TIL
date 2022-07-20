import sys

sys.stdin = open("2050_input.txt", "r")

N = str(input())

for i in range(len(N)):
    print(ord(N[i])-64, end=' ')