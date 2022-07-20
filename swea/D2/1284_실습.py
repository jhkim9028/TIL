import sys

sys.stdin = open("1284_input.txt", "r")

T = int(input())

for i in range(1,T+1):
    P, Q, R, S, W = map(int, input().split())
    B = 0
    A = W * P
    if W <= R:
        B = Q
    else:
        B = Q + (W - R) * S
    if A < B:
        print('#{} {}'.format(i,A))
    else:
        print('#{} {}'.format(i,B))
    