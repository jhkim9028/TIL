from dataclasses import replace
import sys
sys.stdin = open('1547_input.txt')

m = int(input())
ball = 1

for _ in range(m):
    x, y = map(int, input().split())
    if y == ball:
        ball = x
    elif x == ball:
        ball = y
print(ball)