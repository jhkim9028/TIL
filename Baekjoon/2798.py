import sys
input = sys.stdin.readline

n, m = map(int, input().split())

numbers = list(map(int, input().split()))

ans = 0


for i in range(n):

    for j in range(i+1,n):

        for k in range(j+1,n):
            if m >= numbers[i]+numbers[j]+numbers[k] >= ans:
                ans = numbers[i]+numbers[j]+numbers[k]
            else:
                continue
    
print(ans)