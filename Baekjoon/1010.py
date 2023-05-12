import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    a,b = map(int, input().split())
    result = 1
    for i in range(b, b-a,-1):
        result *= i

    resultC = 1
    for i in range(a,0,-1):
        resultC *= i
        

    print(int(result / resultC))