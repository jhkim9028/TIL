from array import array
import sys
sys.stdin = open('2693_input.txt')

T = int(input())

n = 3

for t in range(T):
    array_A = list(map(int, input().split()))
    array_A.sort()
    print(array_A[-3])
        