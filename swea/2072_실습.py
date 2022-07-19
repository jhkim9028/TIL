import sys

sys.stdin = open("2072_input.txt", "r")

T = int(input())


for i in range(T):
    k = list(map(int, input().split()))
    a = 0
    for j in k:
        if j % 2 == 1:
            a += j
    print('#%d %d' % (i+1, a))