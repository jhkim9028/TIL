import sys
input = sys.stdin.readline

n = int(input())

X = []
Y = []

for _ in range(n):
    x,y = map(int, input().split())
    
    X.append(x)
    Y.append(y)
    

a = max(X) - min(X)
b = max(Y) - min(Y)

print(a*b)