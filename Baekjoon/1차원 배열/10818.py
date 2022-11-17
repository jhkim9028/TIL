import sys

sys.stdin = open("10818_input.txt", "r")

N = int(input())


for i in range(1):
    num = list(map(int, input().split()))
print(min(num), max(num))
