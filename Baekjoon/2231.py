import sys
input = sys.stdin.readline

n = int(input())

a = 1

while True:
    ans = 0
    for i in range(len(str(a))):
        ans += int(str(a)[i])
    ans += a
    
    if ans == n:
        break
    if a > n:
        a = 0
        break
    a += 1

print(a)