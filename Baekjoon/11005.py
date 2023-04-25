import sys
input = sys.stdin.readline

N, B = map(int,input().split())
ans = ''
tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while N!=0:
    
    rest = N % B
    N //= B
    ans += tmp[rest]

print(ans[::-1])
