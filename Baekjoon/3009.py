import sys
input = sys.stdin.readline

X = []
Y = []

for _ in range(3):
    x,y = map(int,input().split())
    
    X.append(x)
    Y.append(y)

ans_x = []
ans_y = []
for i in range(3):
    if X.count(X[i]) == 1:
        ans_x.append(X[i])
    if Y.count(Y[i]) == 1:
        ans_y.append(Y[i])

print(*(ans_x+ans_y))