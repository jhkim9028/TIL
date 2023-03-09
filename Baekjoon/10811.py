N,M = map(int, input().split())
num = []

for i in range(N+1):
    num.append(i)


for i in range(M):
    a,b = map(int, input().split())
    stack = []
    for j in range(a,b+1):
        stack.append(num[j])
   
    stack = stack[::-1]
    number = 0
    for k in range(a,b+1):
        num[k] = stack[number]
        number+= 1
print(*num[1::])