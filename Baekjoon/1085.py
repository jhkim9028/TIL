import sys
input = sys.stdin.readline

x,y,w,h = map(int,input().split())

a = abs(0-x)
b = abs(0-y)
c = abs(w-x)
d = abs(h-y)

print(min(a,b,c,d))