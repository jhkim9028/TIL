import sys
sys.stdin = open('5533_input.txt')
from pprint import pprint
N = int(input())

game = [list(map(int, input().split())) for _ in range(N)]


new_game = [[],[],[]]
ans = [[],[],[]]
for i in range(3):
    for j in range(N):
        new_game[i].append(game[j][i])

for i in range(3):
    for j in range(N):
        if new_game[i].count(game[j][i]) > 1:
            ans[i].append(0)
        if new_game[i].count(game[j][i]) == 1:
            ans[i].append(game[j][i])

for i in range(N):
    a = 0
    for j in range(3):
        a += ans[j][i]
    print(a)