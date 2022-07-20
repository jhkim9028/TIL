import sys

sys.stdin = open("2025_input.txt", "r")

N = int(input())

sum = 0
for i in range(1,N+1):
    sum += i
print(sum)