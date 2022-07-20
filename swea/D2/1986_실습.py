import sys

sys.stdin = open("1986_input.txt", "r")

T = int(input())

for i in range(1, T+1):
    N = int(input())
    a = 0
    for j in range(1,N+1):
        if j % 2 == 0:
            a = a - j
        else:
            a = a + j
    print('#%d %d' % (i, a))