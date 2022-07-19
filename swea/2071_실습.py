import sys

sys.stdin = open("2071_input.txt", "r")

T = int(input())

for i in range(T):
    k = list(map(int, input().split()))
    print("#%d %d" % (i+1,round(sum(k)/10)))