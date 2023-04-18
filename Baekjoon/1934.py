import sys
input = sys.stdin.readline

# 최대공약수
def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a


T = int(input())

for t in range(T):
    n1, n2 = map(int,input().split())

    gcd_ = int(gcd(n1,n2))
    ans = int(n1 * (n2/gcd_))
    print(ans)