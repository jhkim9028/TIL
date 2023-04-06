import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())
num = [a,b,c]
m = max(num)

if a == m:
    
    if sum(num) <= a*2:
        while True:
            if b+c > a:
                break
            a -= 1
elif b == m:
    if sum(num) <= b*2:
        while True:
            if a + c > b:
                break
            b -= 1
else:
    if sum(num) <= c*2:
        while True:
            if a + b > c:
                break
            c -= 1

print(a+b+c)