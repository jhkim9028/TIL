import sys
input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    a,b = map(int, input().split())
    
    arr.append([b,a])

arr = sorted(arr)
for i in range(N):
    print(arr[i][1],arr[i][0])