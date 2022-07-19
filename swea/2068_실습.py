import sys

sys.stdin = open("2068_input.txt", "r")

T = int(input())
b = []

for i in range(T):
    k = list(map(int, input().split()))
    a = k[0]
    for j in k:
        if a < j:
            a = j
    print("#%d %d" % (i+1, a))
        