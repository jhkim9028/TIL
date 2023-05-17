import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int,input().split()))

sumNumbers = [0 for _ in range(N)]

sumNumbers[0] = numbers[0]
for n in range(1,N):
    sumNumbers[n] = sumNumbers[n-1] + numbers[n]

for m in range(M):
    a,b = map(int,input().split())
    if a == 1:
        print(sumNumbers[b-1])
    elif a == b:
        print(numbers[a-1])
    else:
        print(sumNumbers[b-1] - sumNumbers[a-2])