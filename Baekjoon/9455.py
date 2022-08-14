import sys
sys.stdin = open('9455_input.txt')
from pprint import pprint

# T = int(input())
# for t in range(T):

n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

new_box = []
for i in range(m):
    new_ = []
    for j in range(n)[::-1]:
        new_.append(box[j][i])
    new_box.append(new_)

