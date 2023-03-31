import sys
input = sys.stdin.readline

n, k = map(int,input().split())


N = 1
for i in range(n-k+1,n+1):
    N *= i

K = 1
for j in range(1,k+1):
    K *= j


print(int(N/K))