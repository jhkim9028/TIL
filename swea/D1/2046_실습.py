import sys

sys.stdin = open("2046_input.txt", "r")

n = int(input())

for i in range(1,n+1):
    print('#', end='')