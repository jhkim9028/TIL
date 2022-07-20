import sys

sys.stdin = open("2058_input.txt", "r")

N = int(input())
result = 0
while N != 0:
    result += N % 10
    N //= 10
print(result)

