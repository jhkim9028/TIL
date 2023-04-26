import sys
input = sys.stdin.readline

def gcd(a,b):
    while b != 0:
        a,b = b, a % b
    return a


a, b = map(int,input().split())
c, d = map(int, input().split())

under = b * d

up1 = a * d
up2 = c * b

up = up1 + up2

gcd = gcd(up, under)

print(int(up/gcd), int(under/gcd))