import sys
input = sys.stdin.readline

def gcd(a,b):
    while b !=0:
        a,b = b, a%b
    return a

A,B = map(int, input().split())

if gcd(A,B) == 1:
    ans = A * B
else:
    ans = A * (B/gcd(A,B))
print(int(ans))