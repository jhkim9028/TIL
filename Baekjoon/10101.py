import sys
input = sys.stdin.readline


A = []
b = 0
ans = ''
for _ in range(3):
    a = int(input())
    
    if a in A:
        ans = 'Isosceles'
    A.append(a)
    if a == 60:
        b += 1


if b == 3:
    print('Equilateral')
    
elif sum(A) == 180:
    if ans == 'Isosceles':
        print(ans)
    else:
        print('Scalene')
else:
    print('Error')